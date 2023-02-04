from flask import Blueprint, jsonify
from apiflask import APIBlueprint

from src.api.controllers.user_controller import getUsers
from src.api.controllers.auth_controller import login,fill_data
from src.api.auth.auth import requires_auth

user_bp = APIBlueprint("user_bp",__name__)

@user_bp.get('/')
# @requires_auth()
def get_user():
    return getUsers()
@user_bp.post('/')
def Login():
    return login()

@user_bp.put('/user')
@requires_auth
def Fill_Data(user):
    return fill_data(user)

@user_bp.route('/<userId>',methods=["GET"])
@requires_auth
def isValid(user,userId):
    return jsonify({"status":"success","data":{"isValid":user.info.address is not None}})

