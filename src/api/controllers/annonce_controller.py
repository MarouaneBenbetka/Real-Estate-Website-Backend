import uuid

from flask import request, make_response, jsonify
from src.api import db
from src.api.models import Annonce


def getAllAnnonces():
    pageNumber = request.args.get("page", 1, int)
    try:
        annonces = Annonce.query.paginate(page=pageNumber, per_page=12)
    except:
        return make_response({"status": "invalid", "data": None, "message": "Invalid page Number"}, 200)
    items = map(lambda annonce: annonce.toJson(), annonces.items)

    return make_response(jsonify(
        {"status": "success", "data": list(items), "message": None, "current_page": pageNumber,
         "max_pages": annonces.total}),
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
            "price" in body) and ("category" in body) and ("commune" in body):
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


def SearchForAnnonce(search_term):
    return "this route in for searching for certain annonce"

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
