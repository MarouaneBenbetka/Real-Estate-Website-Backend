import json
from flask import Blueprint, abort, jsonify, request
from api.controllers.message_controller import getAllMessages, sendMessages
from api.auth.auth import requires_auth


message_bp = Blueprint("message_bp",__name__)


#this route is for getting all the messages
@message_bp.route('/')
def get_all_messages():
    return getAllMessages()


@message_bp.route('/',methods=['POST'])
def send_message():
    return sendMessages()

