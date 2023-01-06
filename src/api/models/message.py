import datetime

from src.api import db
from src.api.models.user import User


class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True,autoincrement=True )
    content = db.Column(db.TEXT)
    seen = db.Column(db.String(1),default='0')
    sender_id = db.Column(db.String(36), nullable=False)
    annonce_id = db.Column(db.String(36), db.ForeignKey("annonces.id"))
    created_at = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    def toJson(self):
        return {"id" : self.id,"message":self.content,"vue":False if self.seen=="1" else True,"date":self.created_at,"name":User.query.filter_by(id=self.sender_id).first().full_name,"photo":User.query.filter_by(id=self.sender_id).first().picture_link}
    def add(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()

