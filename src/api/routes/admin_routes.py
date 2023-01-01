from flask import Blueprint
from api.controllers.admin_controller import ScrapAnnonce
import requests

admin_bp = Blueprint("admin_bp",__name__)


@admin_bp.get('/')
def fetch():
    return ScrapAnnonce()