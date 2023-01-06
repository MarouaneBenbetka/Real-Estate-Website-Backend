from flask import Blueprint
from src.api.controllers.admin_controller import ScrapAnnonce

admin_bp = Blueprint("admin_bp",__name__)


@admin_bp.get('/')
def fetch():
    return ScrapAnnonce()