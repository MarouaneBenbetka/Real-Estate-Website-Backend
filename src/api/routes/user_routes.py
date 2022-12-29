from flask import Blueprint
from api.controllers.api import home


user_bp = Blueprint("user_bp",__name__)
user_bp.get("/")(home)
