import json
from flask import Blueprint, abort, jsonify, request
from api.controllers.user_controller import home
from api.auth.auth import requires_auth
from api.models.annonce import Annonce


annonce_bp = Blueprint("annonce_bp", __name__)


@annonce_bp.route('/annonces')
# @requires_auth("get:drinks-detail")
def get_annonces():
    try:
        annonces = Annonce.query.all()
        return jsonify({
            "success": True,
            "annonces": [annonce.short() for annonce in annonces]
        }), 200
    except:
        abort(422)


'''
ce route c'est pour avoir les details d'une annonce
'''


@annonce_bp.route('/drinks-detail')
@requires_auth("get:drinks-detail")
def get_drinks_detail(jwt):
    try:
        annonces = Annonce.query.all()
        return jsonify({
            "success": True,
            "drinks": [annonce.long() for annonce in annonces]
        }), 200
    except:
        abort(422)


'''
route pour ajouter une annonce
'''
@app.route('/drinks',methods=['POST'])
@requires_auth("post:drinks")
def add_drink(jwt):
    body = request.get_json()

    try:
        title1 = body["title"]
        recipe1 = json.dumps(body['recipe'])
        print(title1 + recipe1)
        annonce = Annonce(title=title1, recipe=recipe1)
        print("hello")
        annonce.insert()
        print("there")
        return jsonify({
        "success":True,
        "annonces": [annonce.long()]
        }),200

    except:
        abort(422)
