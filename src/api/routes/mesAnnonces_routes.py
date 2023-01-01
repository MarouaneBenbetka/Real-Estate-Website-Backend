import json
from flask import Blueprint, abort, jsonify, request
from api.controllers.user_controller import getAnnoncesByUser
from api.auth.auth import requires_auth
from api.models.annonce import Annonce

mesAnnonces_bp = Blueprint("mesAnnonces_bp", __name__)


@mesAnnonces.route('/')
#@require_auth()
def get_annonces():
    return getAnnoncesByUser()