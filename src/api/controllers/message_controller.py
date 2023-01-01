from flask import jsonify, request

from src.api.models import Annonce,Message


def getAllMessages(user):
    messages = []
    for annonce in user.annonces:
        for message in annonce.messages:
            messages.append(message.toJson())
    return jsonify({"status": "success", "data": messages, "message": None})

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
        return jsonify({"status": "success", "data": None, "message": "message sent successfully"})

    else:
        return jsonify({"status": "failed", "data": None, "message": "invalid request"})


