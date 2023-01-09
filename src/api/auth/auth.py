import os

import jwt
from flask import request, jsonify, make_response
from functools import wraps
from src.api.models import User


def requires_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return jsonify({"success": "failed", "message": 'missing token'})
        token = request.headers['Authorization'].split(" ")[1]
        try:
            payload = jwt.decode(token,
                                 os.getenv("TOKEN_SECRET"), algorithms='HS256')
            print(payload)
            user = User.query.filter_by(id=payload["userId"]).first()
            if user is None:
                return make_response(jsonify({"success": "failed", "message": 'Invalid user'}),401)
            if f"/{user.id}/" != request.endpoint:
                if user.address is None or user.phone_number is None:
                    return make_response(jsonify({"status": "failed", "data": {"token": token, "isValid": False},
                                                  "message": "missing phone and address"}, 401))
            return f(user)
        except:
            return make_response(jsonify({"success": "failed", "message": 'Invalid token'}), 401)

    return wrapper
