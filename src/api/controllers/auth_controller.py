
import os
import uuid
import jwt
from flask import request, jsonify, make_response
from src.api.models import User


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
            token = jwt.encode({"userId":id},os.getenv("TOKEN_SECRET"))
            return jsonify({"status":"success","data":token,"message":"missing phone and address"})
        else:
            id = user.id
            token = jwt.encode({"userId":id},os.getenv("TOKEN_SECRET"))
            if user.address is None or user.phone_number is None:
                return make_response(jsonify({"status": "success", "data": {"token":token,"isValid":False}, "message": None}),200)
            return make_response(jsonify({"status":"success","data":{"token":token,"isValid":True},"message":None}),200)
    else:
        return make_response(jsonify({"status":"failed","data":None,"message":"missing data in body"}),400)

def fill_data(user):
    body = request.get_json()
    print(body)
    if "address" in body and "phoneNumber" in body:
        user.phone_number = body["phoneNumber"]
        user.address = body["address"]
        user.add()
        return make_response(jsonify({"status":"success","data":None,"message":None}),200)
    else:
        return make_response(jsonify({"status":"failed","data":None,"message":"missing data in body"}),400)



