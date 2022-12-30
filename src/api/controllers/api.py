import uuid
from functools import wraps

from api.models import Annonce, User
from api import db, app
from flask import make_response, jsonify, request
from api.controllers.auth import auth_required


def getAllAnnonces():
    pageNumber = request.args.get("page", 1, int)
    try:
        annonces = Annonce.query.paginate(page=pageNumber, per_page=12)
    except:
        return make_response({"status": "invalid", "data": None, "message": "Invalid page Number"}, 200)
    l = []
    for annonce in annonces.items:
        l.append(annonce.briefObjToJson())
    return make_response(jsonify(
        {"status": "success", "data": l, "message": None, "current_page": pageNumber, "max_pages": annonces.total}),
                         200)


def getAnnonce(annonceId):
    annonce = Annonce.query.filter_by(id=annonceId).first()
    if annonce == None:
        return make_response(jsonify({"status": "failed", "data": None, "message": "invalid annonce id"}))
    print(annonce.owner)
    return make_response(jsonify({"status": "success", "data": annonce.toJson(), "message": None}))


@auth_required
def getUserAnnonces(user):
    annonces = user.annonces
    l = []
    for annonce in annonces:
        l.append(annonce.briefObjToJson())
    return make_response(jsonify(
        {"status": "success", "data": l, "message": None}), 200)


@auth_required
def addAnnonce(user):
    body = request.get_json()
    print(body)
    if ("typeId" in body) and ("description" in body) and ("surface" in body) and ("wilaya" in body) and (
            "price" in body) and ("category" in body) and ("commune" in body):
        annonce = Annonce()
        annonce.price=body["price"]
        annonce.description = body["description"]
        annonce.wilaya = body["wilaya"]
        annonce.commune = body["commune"]
        annonce.type_id =int( body["typeId"])
        annonce.surface = body["surface"]
        annonce.category = body["category"]
        annonce.id=str(uuid.uuid1())
        annonce.user_id=user.id
        annonce.add()
        return jsonify({"status": "done","data":None,"message":None})
    else:
        return jsonify({"status":"failed","data":None,"message":"missing informations"})

