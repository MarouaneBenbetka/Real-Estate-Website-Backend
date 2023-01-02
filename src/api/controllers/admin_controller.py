import uuid

from flask import jsonify

from src.api import app
from bs4 import BeautifulSoup
import requests

from src.api.models import Annonce, Image, Type


def ScrapAnnonce():
    try:
        response = requests.get("http://www.annonce-algerie.com/upload/flux/rss_1.xml", verify=False)
        items = BeautifulSoup(response.content, "xml").find_all("item")
        for item in items:
            response = requests.get(item.find("link").get_text(), verify=False)
            table = BeautifulSoup(response.content, "html.parser").find_all('table', class_="da_rub_cadre")[1].find_all(
                'tr')
            data = []
            images = BeautifulSoup(response.content, "html.parser").find_all('table', class_="da_rub_cadre")[
                3].find_all(
                'img')

            for tr in table:
                if len(tr.find_all('td', class_=("da_field_text"))) != 0:
                    data.append(tr.find_all('td', class_=("da_field_text"))[0].get_text())
            print(response)
            print(data)
            type = data[0].split(">")[1].strip()
            wilaya = data[2].split(">")[1].strip()
            commune = data[2].split(">")[3].strip()
            i = 0
            if len(data) == 8:
                i += 1
            surface = int(data[3 + i].strip().split("m²")[0].strip().replace(" ", ""))
            price = int(str(data[4 + i].split("Dinar")[0].strip()).replace(" ", ""))
            description = data[5 + i].strip()
            annonce = createAnnonceFromMap(
                {"type": type.lower(), "wilaya": wilaya, "commune": commune, "surface": surface, "price": price,
                 "description": description})
            annonce.add()
            for imageInfo in images:
                image = Image()
                image.annonce_id = annonce.id
                image.link = "http://www.annonce-algerie.com" + imageInfo.get("src")
                image.add()
        return jsonify({"status":"success","data":None,"message":None})
    except:
        return jsonify({"status":"failed","data":None,"message":"error while scrapping"})

def createAnnonceFromMap(map):
    print(map)
    annonce = Annonce()
    annonce.id = str(uuid.uuid1())
    annonce.price = map["price"]
    annonce.surface = map["surface"]
    annonce.wilaya = map["wilaya"]
    annonce.commune = map["commune"]
    annonce.description = map["description"]
    annonce.user_id = None
    type = Type.query.filter_by(name=map["type"]).first()
    if type ==None:
        type = Type()
        type.name = map["type"]
        type.add()
    annonce.type_id = type.id
    return annonce