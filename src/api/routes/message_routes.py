
from flask import Blueprint
from src.api.controllers.message_controller import getAllMessages, sendMessage,viewMessage
from src.api.auth.auth import requires_auth


message_bp = Blueprint("message_bp",__name__)


#this route is for getting all the messages
@message_bp.route('/')
@requires_auth
def get_all_messages(user):
    return getAllMessages(user)

@message_bp.route('/view',methods=['PUT'])
@requires_auth
def view_message(user):
    return viewMessage(user)
@message_bp.route('/',methods=['POST'])
@requires_auth
def send_message(user):
    return sendMessage(user)

