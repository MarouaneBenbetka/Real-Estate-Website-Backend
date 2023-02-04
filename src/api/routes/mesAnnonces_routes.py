import json
from flask import Blueprint
from apiflask import APIBlueprint

from src.api.controllers.user_controller import getAnnoncesByUser
from src.api.auth.auth import requires_auth

mesAnnonces_bp = APIBlueprint("mesAnnonces_bp", __name__)


@mesAnnonces_bp.route('/')
@requires_auth
def get_annonces(user):
    return getAnnoncesByUser(user)