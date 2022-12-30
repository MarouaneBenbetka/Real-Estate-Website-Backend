from flask import Blueprint
from api.controllers.api import getAllAnnonces,getAnnonce,getUserAnnonces,addAnnonce
user_bp = Blueprint("user_bp",__name__)

user_bp.get("/getAllAnnonces")(getAllAnnonces)
user_bp.get("/annonce/<annonceId>")(getAnnonce)
user_bp.get("/user/annonces")(getUserAnnonces)
user_bp.post("/addAnnonce")(addAnnonce)
