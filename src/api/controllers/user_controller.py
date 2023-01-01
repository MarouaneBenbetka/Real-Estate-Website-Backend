from flask import jsonify, make_response
from src.api import db
from src.api.models.annonce import Annonce
from src.api.models import User


def getUsers():
    return jsonify( {"status":"success","data":list(map(lambda user:user.toJson(),User.query.all())),"message":None})


def getAnnoncesByUser(user):
    annonces = user.annonces
    items = map(lambda annonce: annonce.toJson(), annonces)
    return make_response(jsonify(
        {"status": "success", "data": list(items), "message": None}), 200)