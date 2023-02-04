import math

from flask import jsonify, make_response, request
from src.api import db
from src.api.models.annonce import Annonce
from src.api.models import User


def getUsers():
    return make_response(jsonify( {"status":"success","data":list(map(lambda user:user.toJson(),User.query.all())),"message":None}),200)


def getAnnoncesByUser(user):
    pageNumber = request.args.get("page", 1, int)

    annonces = user.annonces.paginate(page=pageNumber, per_page=12)

    items = map(lambda annonce: annonce.toJson(), annonces.items)
    return make_response(jsonify({"status": "success", "data": list(items), "message": None, "current_page": pageNumber,
         "max_pages": math.ceil(annonces.total / 12)}), 200)