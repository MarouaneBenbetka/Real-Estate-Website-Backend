from flask import Blueprint
from apiflask import APIBlueprint

from src.api.controllers.admin_controller import ScrapAnnonce,get_website_stats

admin_bp = APIBlueprint("admin_bp",__name__)


@admin_bp.get('/')
def fetch():
    return ScrapAnnonce()
@admin_bp.get('/stats')
def getStats():
    return get_website_stats()