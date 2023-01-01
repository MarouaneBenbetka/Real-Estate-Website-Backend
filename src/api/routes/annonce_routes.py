import json
from flask import Blueprint, abort, jsonify, request
from src.api.controllers.annonce_controller import AddAnnonce,DeleteAnnonce, getAllAnnonces, getAnnonceDetails, SearchForAnnonce
from src.api.auth.auth import requires_auth
from src.api.models.annonce import Annonce


annonce_bp = Blueprint("annonce_bp", __name__)


@annonce_bp.route('/annonces')
# @requires_auth()
def get_annonces():
    return getAllAnnonces()

'''
ce route c'est pour avoir les details d'une annonce
'''


@annonce_bp.route('/<annonceId>')
def get_Annonce_Details(annonceId):
    return getAnnonceDetails(annonceId)

'''
route pour ajouter une annonce
'''
@annonce_bp.route('/',methods=['POST'])
@requires_auth()
def Add_Annonce(user):
    return Add_Annonce(user)


'''
route pour supprimer une annonce
'''
@annonce_bp.route('/',methods=['DELETE'])
@requires_auth()
def Delete_Annonce(user):
    return DeleteAnnonce(user)
