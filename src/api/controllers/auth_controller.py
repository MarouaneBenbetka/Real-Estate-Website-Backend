import math
import uuid
from datetime import datetime
import jwt
from flask import request, make_response, jsonify
from src.api import db
from src.api.models import Annonce, Type, User


def login():
    body = request.get_json()
    if "email" in body and "image" in body and "name" in body:
        user = User.query.filter_by(email=body["email"]).first()
        if user is None:
            user = User()
            user.email = body["email"]
            user.picture_link = body["image"]
            user.full_name = body["name"]
            id = str(uuid.uuid1())
            user.id = id
            user.add()
            token = jwt.encode({"userId":id},"28472B4B62506553")
            return jsonify({"status":"success","data":token,"message":"missing phone and address"})
        else:
            id = user.id
            token = jwt.encode({"userId":id},"28472B4B62506553")
            if user.address is None or user.phone_number in None:
                return jsonify({"status": "success", "data": token, "message": "missing phone and address"})
            return jsonify({"status":"success","data":token,"message":None})
    else:
        return jsonify({"status":"failed","data":None,"message":"missing data in body"})

def fill_data(user):
    body = request.get_json()
    if "address" in body and "phoneNumber" in body:
        user.phone_number = body["phoneNumber"]
        user.address = body["address"]
        user.add()
    else:
        return jsonify({"status":"failed","data":None,"message":"missing data in body"})



