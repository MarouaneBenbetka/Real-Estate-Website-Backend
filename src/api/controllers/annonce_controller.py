import math
import uuid
from datetime import datetime

from flask import request, make_response, jsonify
from src.api import db
from src.api.models import Annonce, Type


def getAllAnnonces():
    pageNumber = request.args.get("page", 1, int)
    try:
        annonces = Annonce.query.paginate(page=pageNumber, per_page=12)
    except:
        return make_response({"status": "invalid", "data": None, "message": "Invalid page Number"}, 200)
    items = map(lambda annonce: annonce.toJson(), annonces.items)

    return make_response(jsonify(
        {"status": "success", "data": list(items), "message": None, "current_page": pageNumber,
         "max_pages": math.ceil(annonces.total / 12)}),
        200)

def getAnnonceDetails(annonce_id):
    annonce = Annonce.query.filter_by(id=annonce_id).first()
    if annonce == None:
        return make_response(jsonify({"status": "failed", "data": None, "message": "invalid annonce id"}))
    return make_response(jsonify({"status": "success", "data": annonce.toJson(), "message": None}))

def AddAnnonce(user):
    body = request.get_json()
    print(body)
    if ("typeId" in body) and ("description" in body) and ("surface" in body) and ("wilaya" in body) and (
            "price" in body) and ("category" in body) and ("commune" in body) and ("images" in body) and ("coordinates" in body):
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
        return jsonify({"status": "done", "data": None, "message": None})
    else:
        return jsonify({"status": "failed", "data": None, "message": "missing informations"})


def SearchForAnnonce():
    page = request.args.get("page", 1, int)
    minDate = request.args.get("min_date", datetime.date.min)
    maxDate = request.args.get("max_date", datetime.date.max)
    text = request.args.get("q","")
    wilaya = request.args.get("wilaya",None)
    commune = request.args.get("commune",None)
    typeName = request.args.get("type",None)
    annonces = None
    if typeName==None:
        try:
            annonces = Annonce.query.filter(
                db.and_(Annonce.date >= minDate, Annonce.date <= maxDate, Annonce.description.like(f"%{text}%"),
                        Annonce.wilaya.like("%%" if wilaya == None else wilaya),
                        Annonce.wilaya.like("%%" if commune == None else commune))).paginate(
                per_page=12, page=page)
        except:
            return make_response({"status": "invalid", "data": None, "message": "Invalid page Number"}, 200)

    else:
        type = Type.query.filter_by(name=typeName).first()
        try:
            annonces = Annonce.query.filter(
                db.and_(Annonce.date >= minDate, Annonce.date <= maxDate, Annonce.description.like(f"%{text}%"),
                        Annonce.wilaya.like("%%" if wilaya == None else wilaya),
                        Annonce.wilaya.like("%%" if commune == None else commune),
                        Annonce.type_id == type.id)).paginate(
                per_page=12, page=page)
        except:
            return make_response({"status": "invalid", "data": None, "message": "Invalid page Number"}, 200)

    return jsonify({"status":"success","page":page,"max_pages": math.ceil(annonces.total / 12),"message":None,"data": list(map(lambda annonce: annonce.toJson(), annonces.items))})

def DeleteAnnonce(user):
    body = request.get_json()
    if "annonceId" in body:
        annonce = Annonce.query.filter(db.and_(Annonce.id == body["annonceId"], Annonce.user_id == user.id)).first()
        if annonce == None:
            return jsonify({"status": "failed", "data": None, "message": "invalid request"})
        annonce.delete()
        return jsonify({"status": "done", "data": None, "message": None})
    else:
        return jsonify({"status": "failed", "data": None, "message": "invalid request"})
