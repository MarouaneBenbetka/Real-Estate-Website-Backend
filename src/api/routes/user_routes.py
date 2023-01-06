from flask import Blueprint
from src.api.controllers.user_controller import getUsers


user_bp = Blueprint("user_bp",__name__)

@user_bp.route('/')
# @requires_auth()
def get_user():
    return getUsers()


