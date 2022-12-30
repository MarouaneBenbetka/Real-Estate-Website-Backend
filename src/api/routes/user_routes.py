from flask import Blueprint, jsonify
from api.controllers.user_controller import home
from api.auth.auth import requires_auth


user_bp = Blueprint("user_bp",__name__)

@user_bp.route('/')
# @requires_auth("get:drinks-detail")
def get_user():
    return jsonify({'user':"hi"})
#user_bp.get("/")(home)
