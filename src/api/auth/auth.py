import json

import jwt
from flask import abort, request, jsonify
from functools import wraps
from urllib.request import urlopen
import os

from sqlalchemy import true

from src.api import app
from src.api.models import User

AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN")
ALGORITHMS = [os.environ.get("ALGORITHMS")]
API_AUDIENCE = os.environ.get("API_AUDIENCE")


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# Auth Header

'''
extrait le token du header de la requete
'''


def get_token_auth_header():
    pass



'''
check des permissions dans le token
'''


# def check_permissions(permission, payload):
#     if 'permissions' not in payload:
#         raise AuthError({'code': 'invalid payload',
#                          'description': 'your payload sent in the token does not contain permissions list'}, 400)

#     if permission not in payload['permissions']:
#         raise AuthError({'code': 'unauthorized',
#                          'description': 'permission not found in the payload'}, 403)

#     return True


'''
verifie le token issue de auth0'''


def verify_decode_jwt(token):
    pass
    # jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    # jwks = json.loads(jsonurl.read())
    # unverified_header = jwt.get_unverified_header(token)
    # rsa_key = {}

    # if 'kid' not in unverified_header:
    #     raise AuthError({
    #         'code': 'invalid_header',
    #         'description': 'Authorization malformed.'
    #     }, 401)

    # for key in jwks["keys"]:
    #     if key["kid"] == unverified_header["kid"]:
    #         rsa_key = {
    #             "kty": key["kty"],
    #             "kid": key["kid"],
    #             "use": key["use"],
    #             "n": key["n"],
    #             "e": key["e"]
    #         }
    # if rsa_key:
    #     try:
    #         payload = jwt.decode(
    #             token,
    #             rsa_key,
    #             algorithms=ALGORITHMS,
    #             audience=API_AUDIENCE,
    #             issuer='https://' + AUTH0_DOMAIN + '/'
    #         )

    #         return payload

    #     except jwt.ExpiredSignatureError:
    #         raise AuthError({
    #             'code': 'token_expired',
    #             'description': 'Token expired.'
    #         }, 401)

    #     except jwt.JWTClaimsError:
    #         raise AuthError({
    #             'code': 'invalid_claims',
    #             'description': 'Incorrect claims. Please, check the audience and issuer.'
    #         }, 401)
    #     except Exception:
    #         # print(traceback.format_exc())
    #         raise AuthError({
    #             'code': 'invalid_header',
    #             'description': 'Unable to parse authentication token.'
    #         }, 400)
    # raise AuthError({
    #     'code': 'invalid_header',
    #             'description': 'Unable to find the appropriate key.'
    # }, 400)


'''
c'est un decorateur a utiliser dans les routes pour verifier l'auth
'''


def requires_auth(f):
    @wraps(f)
    def wrapper():
        if 'Authorization' not in request.headers:
            return jsonify({"success": "failed", "message": 'missing token'})
        token = request.headers['Authorization']
        try:
            payload = jwt.decode("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiUmF5YW5lIEtlYmlyIiwiZW1haWwiOiJyYXlhbmVrZWIzMkBnbWFpbC5jb20iLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUVkRlRwNmFVVlNMVmd3NXhRdllhU2oyNFBxXzVZVy1UcVVzVF9ZalVFbGY9czk2LWMiLCJzdWIiOiIxMDgyNzY2OTMxMTcwNzU0NTM1NTQiLCJpYXQiOjE2NzI3NjUyODF9.9poVbq3JtzxzhMoLjqS8W3EfygxbpYBnVuh4l9iEJwI", "28472B4B62506553", algorithms='HS256')
            user = User.query.filter_by(email=payload["email"]).first()
            if user==None:
                return jsonify({"success": "failed", "message": 'Invalid user'})
            return f(user)
        except:
            return jsonify({"success": "failed", "message": 'Invalid token'})

    return wrapper
