
import os
import uuid
import jwt
from flask import request, jsonify, make_response
from src.api.models import User, ContactInfo


def login():
    body = request.get_json()
    if "email" in body and "image" in body and "name" in body:
        user = User.query.filter_by(email=body["email"]).first()
        if user is None:
            user = User()
            user.email = body["email"]
            user.picture_link = body["image"]
            user.full_name = body["name"]
            contactInfo = ContactInfo()
            contactInfo.email = body["email"]
            contactInfo.full_name = body["name"]
            contactInfo.add()
            id = str(uuid.uuid1())
            user.id = id
            user.contact_info_id = contactInfo.id
            user.add()
            token = jwt.encode({"userId":id},os.getenv("TOKEN_SECRET"))
            return make_response(
                jsonify({"status": "success", "data": {"token": token, "isValid": False}, "message": None}), 200)
        else:
            id = user.id
            token = jwt.encode({"userId":id},os.getenv("TOKEN_SECRET"))

            return make_response(jsonify({"status":"success","data":{"token":token,"isValid":True},"message":None}),200)
    else:
        return make_response(jsonify({"status":"failed","data":None,"message":"missing data in body"}),400)

def fill_data(user):
    body = request.get_json()
    print(body)
    if "address" in body and "phoneNumber" in body:
        contactInfo = ContactInfo.query.filter_by(id=user.contact_info_id).first()
        contactInfo.phone_number = body["phoneNumber"]
        contactInfo.address = body["address"]
        contactInfo.add()
        user.contact_info_id = contactInfo.id

        return make_response(jsonify({"status":"success","data":None,"message":None}),200)
    else:
        return make_response(jsonify({"status":"failed","data":None,"message":"missing data in body"}),400)



