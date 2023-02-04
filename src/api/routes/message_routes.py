
from apiflask import APIBlueprint
from src.api.controllers.message_controller import getAllMessages, sendMessage,viewMessage,unSeenMessagesCount
from src.api.auth.auth import requires_auth


message_bp = APIBlueprint("message_bp",__name__)


#this route is for getting all the messages
@message_bp.get('/')
@requires_auth
def get_all_messages(user):
    return getAllMessages(user)
@message_bp.get('/unseen')
@requires_auth
def get_unseen_messages_count(user):
    return unSeenMessagesCount(user)

@message_bp.route('/view',methods=['PUT'])
@requires_auth
def view_message(user):
    return viewMessage(user)
@message_bp.post('/')
@requires_auth
def send_message(user):
    return sendMessage(user)

