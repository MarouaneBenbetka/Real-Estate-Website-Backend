from flask import Blueprint, jsonify
from src.api.controllers.user_controller import getUsers
from src.api.controllers.auth_controller import login,fill_data
from src.api.auth.auth import requires_auth

user_bp = Blueprint("user_bp",__name__)

@user_bp.route('/')
# @requires_auth()
def get_user():
    return getUsers()
@user_bp.route('/',methods=["POST"])
def Login():
    return login()

@user_bp.route('/user',methods=["PUT"])
@requires_auth
def Fill_Data(user):
    return fill_data(user)

@user_bp.route('/<userId>',methods=["GET"])
@requires_auth
def isValid(user):
    return jsonify({"status":"success","data":{"isValid":user.address is None}})

