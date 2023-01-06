
import jwt
from flask import abort, request, jsonify
from functools import wraps
from src.api.models import User

def requires_auth(f):
    @wraps(f)
    def wrapper():
        if 'Authorization' not in request.headers:
            return jsonify({"success": "failed", "message": 'missing token'})
        token = request.headers['Authorization']
        try:
            payload = jwt.decode(token,
                "28472B4B62506553", algorithms='HS256')
            print(payload)
            user = User.query.filter(User.email==payload["email"]).first()
            if user is None:
                return jsonify({"success": "failed", "message": 'Invalid user'})
            return f(user)
        except:
            return jsonify({"success": "failed", "message": 'Invalid token'})

    return wrapper
