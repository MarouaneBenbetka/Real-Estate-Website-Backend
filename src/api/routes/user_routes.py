from flask import Blueprint, jsonify
from api.controllers.user_controller import getUsers
from api.auth.auth import requires_auth


user_bp = Blueprint("user_bp",__name__)

@user_bp.route('/')
# @requires_auth()
def get_user():
    return getUsers()
