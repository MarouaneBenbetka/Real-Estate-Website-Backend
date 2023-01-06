import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] =database_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "dsqhjvfqsjnchbrehvfdsfsd"
db = SQLAlchemy(app)

from src.api.routes import *
app.register_blueprint(user_bp,url_prefix="/users")
app.register_blueprint(annonce_bp,url_prefix="/annonces")
app.register_blueprint(message_bp,url_prefix="/messages")
app.register_blueprint(admin_bp,url_prefix="/admin")
app.register_blueprint(mesAnnonces_bp,url_prefix="/mesannonces")




