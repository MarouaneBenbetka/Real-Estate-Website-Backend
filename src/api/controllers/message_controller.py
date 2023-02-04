import math

from flask import jsonify, request, make_response

from src.api.models import Annonce,Message
from src.api import db



def getAllMessages(user):
    page = request.args.get("page",1,int)
    annoncesIds = []
    for annonce in user.annonces:
        annoncesIds.append(annonce.id)
    try:
        messages = Message.query.filter(Message.annonce_id.in_(annoncesIds)).paginate(per_page=25,page=page)
        return make_response(jsonify({"current_page":page,"max_pages":math.ceil(messages.total / 12),"status": "success", "data": list(map(lambda message:message.toJson(),messages.items)), "message": None}),200)
    except:
        return make_response({"status": "failed", "data": None, "message": "Invalid page Number"}, 404)


def viewMessage(user):
    messageId = request.get_json()["messageId"]
    if messageId is None:
        return make_response(jsonify({"status": "failed", "data": None, "message": "missing data"}),400)
    message = Message.query.filter_by(id = int(messageId)).first()
    if message is None:
        return make_response(jsonify({"status": "failed", "data": None, "message": "message does not exist"}),400)
    message.seen="0"
    message.add()
    return make_response(jsonify({"status":"success","data":None,"message":None}),200)

def sendMessage(user):
    body = request.get_json()
    if ("annonceId" in body) and ("content" in body):
        annonce = Annonce.query.filter_by(id=body["annonceId"]).first()
        if(annonce==None):
            return jsonify({"status": "failed", "data": None, "message": "invalid request"})
        if(annonce.user_id==user.id):
            return jsonify({"status": "failed", "data": None, "message": "invalid request can't send message to yourself"})
        message = Message()
        message.content = body["content"]
        message.annonce_id = body["annonceId"]
        message.sender_id = user.id
        message.add()
        return make_response(jsonify({"status": "success", "data": None, "message": "message sent successfully"}),200)

    else:
        return make_response(jsonify({"status": "failed", "data": None, "message": "invalid request"}),400)
def unSeenMessagesCount(user):
    annoncesIds = []
    for annonce in user.annonces:
        annoncesIds.append(annonce.id)
    messages = Message.query.filter(db.and_(Message.annonce_id.in_(annoncesIds),Message.seen=='0')).all()
    return make_response(jsonify(
        { "status": "success", "data": len(messages), "message": None}), 200)


