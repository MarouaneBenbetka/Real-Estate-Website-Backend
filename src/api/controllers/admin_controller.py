import uuid
import datetime

from flask import jsonify, make_response

from src.api import  db
from bs4 import BeautifulSoup
import requests
from src.api.auth.auth import requires_auth
from src.api.models import Annonce, Image, Type, ContactInfo, Message
@requires_auth
def ScrapAnnonce(user):
    if(user.role=="1"):
        return make_response(jsonify({"status": "failed", "data": None, "message": "not admin"}),401)
    try:
        response = requests.get("http://www.annonce-algerie.com/upload/flux/rss_1.xml", verify=False)
        items = BeautifulSoup(response.content, "xml").find_all("item")
        for item in items:
            response = requests.get(item.find("link").get_text(), verify=False)
            table = BeautifulSoup(response.content, "html.parser").find_all('table', class_="da_rub_cadre")[1].find_all(
                'tr')
            phoneNumberInfo = BeautifulSoup(response.content, "html.parser").find_all('table', class_="da_contact")[
                0].find_all("span", class_="da_contact_value")
            phoneNumber = None
            if len(phoneNumberInfo) != 0:
                phoneNumber = phoneNumberInfo[0].get_text().replace(" ", "").replace("+", "").replace("213",
                                                                                                      "").replace("+33",
                                                                                                                  "0")
            addressInfo = BeautifulSoup(response.content, "html.parser").find_all('table', class_="da_contact")[
                0].find_all("span", class_="da_contact_adr_soc")
            ownerAddress = None
            if len(addressInfo):
                ownerAddress = addressInfo[0].get_text()
            nameInfo = BeautifulSoup(response.content, "html.parser").find_all('table', class_="da_contact")[
                0].find_all("span", class_="da_contact_rais_soc")
            name = None
            if len(nameInfo):
                name = nameInfo[0].get_text()

            data = []
            images = BeautifulSoup(response.content, "html.parser").find_all('table', class_="da_rub_cadre")[
                3].find_all(
                'img')

            for tr in table:
                if len(tr.find_all('td', class_=("da_field_text"))) != 0:
                    data.append(tr.find_all('td', class_=("da_field_text"))[0].get_text())
            category = data[0].split(">")[1].strip()
            if category not in ["Vente", "Echange", "Location", "Location vacances"]:
                continue
            type = data[0].split(">")[2].strip()
            wilaya = data[2].split(">")[1].strip()
            wilaya = wilaya.replace("é", "e")
            wilaya = wilaya.replace("è", "e")
            wilaya = wilaya.replace("à", "a")
            commune = data[2].split(">")[3].strip()
            commune=commune.replace("é", "e")
            commune = commune.replace("è", "e")
            commune = commune.replace("à", "a")
            address = None
            i = 0
            if len(data) == 8:
                i += 1
                address = str(data[3].strip())
            surface = int(data[3 + i].strip().split("m²")[0].strip().replace(" ", ""))
            price = int(str(data[4 + i].split("Dinar")[0].strip()).replace(" ", ""))
            description = data[5 + i].strip()
            date = data[6 + i]
            annonce = createAnnonceFromMap(
                {"type": type.lower(), "wilaya": wilaya, "commune": commune, "surface": surface, "price": price,
                 "description": description, "category": category, "address": address, "date": date,"phoneNumber":phoneNumber,"name":name,"ownerAddress":ownerAddress})
            annonce.add()
            for imageInfo in images:
                image = Image()
                image.annonce_id = annonce.id
                image.link = "http://www.annonce-algerie.com" + imageInfo.get("src")
                image.add()
        return make_response(jsonify({"status":"success","data":None,"message":None}),200)
    except:
        return make_response(jsonify({"status": "failed", "data": None, "message": "problem while scrapping"}),501)


def createAnnonceFromMap(map):
    annonce = Annonce()
    contactInfo = ContactInfo()
    contactInfo.address = map["ownerAddress"]
    contactInfo.phone_number = map["phoneNumber"]
    contactInfo.full_name = map["name"]
    contactInfo.add()
    annonce.id = str(uuid.uuid1())
    annonce.price = map["price"]
    annonce.surface = map["surface"]
    annonce.wilaya = map["wilaya"]
    annonce.commune = map["commune"]
    annonce.category = map["category"]
    annonce.description = map["description"]
    annonce.address = map["address"]
    dates = map["date"].split("/")
    annonce.date = datetime.date(int(dates[2]), int(dates[1]), int(dates[0]) )
    annonce.user_id = None
    annonce.contact_info_id = contactInfo.id
    type = Type.query.filter_by(name=map["type"]).first()
    if type == None:
        type = Type()
        type.name = map["type"]
        type.add()
    annonce.type_id = type.id
    return annonce
@requires_auth
def get_website_stats(user):
    if (user.role == "1"):
        return make_response(jsonify({"status": "failed", "data": None, "message": "not admin"}), 401)
    return make_response(jsonify({"data":{"annonces_count":len(Annonce.query.all()),"messages_count":len(Message.query.all())},"message":None,"status":"success",}),200)