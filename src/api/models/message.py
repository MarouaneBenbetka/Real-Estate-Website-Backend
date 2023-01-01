import datetime
import json
from src.api import db
class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True,autoincrement=True )
    content = db.Column(db.TEXT)
    seen = db.Column(db.String(1),default='0')
    sender_id = db.Column(db.String(36), nullable=False)
    annonce_id = db.Column(db.String(36), db.ForeignKey("annonces.id"))
    created_at = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    def toJson(self):
        return {"id" : self.id,"content":self.content,"seen":self.seen,"created_at":self.created_at}
    def add(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()

