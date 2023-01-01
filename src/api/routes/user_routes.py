from flask import Blueprint, jsonify
from src.api.controllers.user_controller import getUsers
from src.api.controllers.auth import auth_required


user_bp = Blueprint("user_bp",__name__)

@user_bp.route('/')
# @requires_auth()
def get_user():
    return getUsers()


