import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
import sys



app = Flask(__name__)
# setup_db(app)


@app.route('/annonces')
def get_annonces():
    try:
        annonces = Annonce.query.all()
        return jsonify({
        "success":True,
        "annonces": [annonce.short() for annonce in annonces]
        }),200
    except:
        abort(422)




#error handlers

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def wrongRequest(error):
    return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
            }), 404

@app.errorhandler(AuthError)
def AuthError(error):
    return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
    }), error.status_code