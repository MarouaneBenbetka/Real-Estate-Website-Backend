import os

from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from api.routes import *

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = database_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.register_blueprint(user_bp, url_prefix='/users')
db = SQLAlchemy(app)


