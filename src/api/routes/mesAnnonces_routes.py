import json
from flask import Blueprint, abort, jsonify, request
from src.api.controllers.user_controller import getAnnoncesByUser
from src.api.controllers.auth import auth_required
from src.api.models.annonce import Annonce

mesAnnonces_bp = Blueprint("mesAnnonces_bp", __name__)


@mesAnnonces_bp.route('/')
@auth_required
def get_annonces(user):
    return getAnnoncesByUser(user)