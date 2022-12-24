import os
from setuptools import setup
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

db = SQLAlchemy()


#setup db : configuration de la base de donnees

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

#drop and create all : pour reinestialiser la base de donnees

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()



# les classes



# machine abstraite de la BDD

   '''
    insert()
        inserer une nouvelle ligne dans la BDD
        EXAMPLE
            annonce = Annonce(title=req_title, recipe=req_recipe)
            annonce.insert()
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        supprimer ligne dans la BDD

        EXAMPLE
            annonce = Annonce(title=req_title, recipe=req_recipe)
            annonce.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        mettre a jour ligne dans la BDD

        EXAMPLE
            annonce = Annonce.query.filter(Annonce.id == id).one_or_none()
            annonce.title = 'Black Coffee'
            annonce.update()
    '''
    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())

