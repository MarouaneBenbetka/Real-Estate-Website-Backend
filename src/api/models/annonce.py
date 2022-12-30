import json
from api import db
class Annonce(db.Model):
    __tablename__ = "annonces"
    id = db.Column(db.String(36), primary_key=True, nullable=False, unique=True )
    category = db.Column(db.String(1))
    surface = db.Column(db.Float)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    wilaya = db.Column(db.String(2))
    commune = db.Column(db.String(30))
    address = db.Column(db.String(50))
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"))
    type_id = db.Column(db.Integer, db.ForeignKey("types.id"))
    images = db.relationship("Image", backref="annonce", lazy=False)
    def briefObjToJson(self):
        return {"id": self.id, "category": self.category, "description": self.description,
                "price": self.price
            , "wilaya": self.wilaya, "commune": self.commune,
                "type": self.type_id
                }
    def toJson(self):
        return {"id" : self.id,"category":self.category,"surface":self.surface,"description":self.description,"price":self.price
                       ,"wilaya":self.wilaya,"commune":self.commune,"address":self.address,"owner_id":self.user_id,"type":self.type_id
        }
    def add(self):
        db.session.add(self)
        db.session.commit()

