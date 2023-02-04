import os
from apiflask import APIFlask
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS
from flask_swagger import swagger

load_dotenv()
database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))
app = APIFlask(__name__, docs_ui='swagger-ui',docs_path='/docs')


CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] =os.getenv("DATABASE_URI")#database_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "dsqhjvfqsjnchbrehvfdsfsd"
db = SQLAlchemy(app)

from src.api.routes import *
app.register_blueprint(user_bp,url_prefix="/users")
app.register_blueprint(annonce_bp,url_prefix="/annonces")
app.register_blueprint(message_bp,url_prefix="/messages")
app.register_blueprint(admin_bp,url_prefix="/admin")
app.register_blueprint(mesAnnonces_bp,url_prefix="/mesannonces")
@app.route('/swagger.json')
def swagger_json():
    return swagger
def create_app():
    app = APIFlask(__name__)
    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] =os.getenv("DATABASE_URI")#database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "dsqhjvfqsjnchbrehvfdsfsd"
    db = SQLAlchemy(app)
    app.register_blueprint(user_bp,url_prefix="/users")
    app.register_blueprint(annonce_bp,url_prefix="/annonces")
    app.register_blueprint(message_bp,url_prefix="/messages")
    app.register_blueprint(admin_bp,url_prefix="/admin")
    app.register_blueprint(mesAnnonces_bp,url_prefix="/mesannonces")
    return app


