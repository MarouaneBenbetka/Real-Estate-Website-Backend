import json
from flask import Blueprint, abort, jsonify, request
from src.api.controllers.message_controller import getAllMessages, sendMessage
from src.api.controllers.auth import auth_required


message_bp = Blueprint("message_bp",__name__)


#this route is for getting all the messages
@message_bp.route('/')
@auth_required
def get_all_messages(user):
    return getAllMessages(user)


@message_bp.route('/',methods=['POST'])
@auth_required
def send_message(user):
    return sendMessage(user)

