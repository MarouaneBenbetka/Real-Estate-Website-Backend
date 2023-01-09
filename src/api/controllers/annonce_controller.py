import math
import uuid
import datetime

from flask import request, make_response, jsonify
from src.api import db
from src.api.models import Annonce, Type, Image


def getAllAnnonces():
    pageNumber = request.args.get("page", 1, int)
    try:
        annonces = Annonce.query.paginate(page=pageNumber, per_page=12)
    except:
        return make_response({"status": "invalid", "data": None, "message": "Invalid page Number"}, 404)
    items = map(lambda annonce: annonce.briefObjToJson(), annonces.items)

    return make_response(jsonify(
        {"status": "success", "data": list(items), "message": None, "current_page": pageNumber,
         "max_pages": math.ceil(annonces.total / 12)}),
        200)

def getAnnonceDetails(annonce_id):
    annonce = Annonce.query.filter_by(id=annonce_id).first()
    if annonce == None:
        return make_response(jsonify({"status": "failed", "data": None, "message": "invalid annonce id"}),400)
    return make_response(jsonify({"status": "success", "data": annonce.toJson(), "message": None}),200)

def AddAnnonce(user):
    body = request.get_json()
    print(body)
    if ("typeId" in body) and ("description" in body) and ("surface" in body) and ("wilaya" in body) and (
            "price" in body) and ("category" in body) and ("commune" in body) and ("images" in body) and ("coordinates" in body) and ("images" in body):
        annonce = Annonce()
        annonce.price = body["price"]
        annonce.description = body["description"]
        annonce.wilaya = body["wilaya"]
        annonce.commune = body["commune"]
        annonce.type_id = int(body["typeId"])
        annonce.surface = body["surface"]
        annonce.category = body["category"]
        annonce.id = str(uuid.uuid1())
        annonce.user_id = user.id
        annonce.add()
        for image_link in body["images"]:
            image = Image()
            image.annonce_id = annonce.id
            image.link = image_link
            image.add()

        return make_response(jsonify({"status": "done", "data": None, "message": None}),200)
    else:
        return make_response(jsonify({"status": "failed", "data": None, "message": "missing informations"}),400)


def SearchForAnnonce():
    page = request.args.get("page", 1, int)
    minDate = request.args.get("min_date", datetime.date.min)
    maxDate = request.args.get("max_date", datetime.date.max)
    if minDate=="":
        minDate = datetime.date.min
    if maxDate=="":
        maxDate = datetime.date.max

    text = request.args.get("q","")
    wilaya = request.args.get("wilaya","%%")
    commune = request.args.get("commune","%%")
    typeName = request.args.get("type","%%")
    try:
        annonces = Annonce.query.filter(
            db.and_(Annonce.date >= minDate, Annonce.date <= maxDate, Annonce.description.like(f"%{text}%"),
                    Annonce.wilaya.like(f"%{wilaya}%"),
                    Annonce.wilaya.like(f"%{commune}%"),Annonce.category.like(f"%{typeName}%"))).paginate(
            per_page=12, page=page)
        return make_response(jsonify(
            {"status": "success", "page": page, "max_pages": math.ceil(annonces.total / 12), "message": None,
             "data": list(map(lambda annonce: annonce.toJson(), annonces.items))}), 200)

    except:
        return make_response({"status": "invalid", "data": None, "message": "Invalid page Number"}, 404)


def DeleteAnnonce(user):
    body = request.get_json()
    if "annonceId" in body:
        annonce = Annonce.query.filter(db.and_(Annonce.id == body["annonceId"], Annonce.user_id == user.id)).first()
        if annonce == None:
            return make_response(jsonify({"status": "failed", "data": None, "message": "invalid request"}),400)
        annonce.delete()
        return jsonify({"status": "done", "data": None, "message": None})
    else:
        return make_response(jsonify({"status": "failed", "data": None, "message": "invalid request"}),400)
