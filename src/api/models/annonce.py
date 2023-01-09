
from src.api import db
from src.api.models.user import User
from src.api.models.type import Type


class Annonce(db.Model):
    __tablename__ = "annonces"
    id = db.Column(db.String(36), primary_key=True, nullable=False, unique=True )
    category = db.Column(db.String(30))
    surface = db.Column(db.Float)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    wilaya = db.Column(db.String(30))
    commune = db.Column(db.String(30))
    address = db.Column(db.String(255))
    date = db.Column(db.Date)
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"))
    type_id = db.Column(db.Integer, db.ForeignKey("types.id"))
    images = db.relationship("Image", backref="annonce", lazy=False)
    latitude = db.Column(db.String(30))
    longitude = db.Column(db.String(30))
    def briefObjToJson(self):
        return {"id": self.id, "typeAnnonce": self.category, "description": self.description,
                "prix": self.price
            , "wilaya": self.wilaya, "commune": self.commune,
                "typeImmoblier": Type.query.filter_by(id=self.type_id).first().name,"images":list(map(lambda image:image.link,self.images))
                }
    def toJson(self):
        return {"id" : self.id,"typeAnnonce":self.category,"surface":self.surface,"description":self.description,"prix":self.price
                       ,"wilaya":self.wilaya,"commune":self.commune,"address":self.address,"typeImmoblier":Type.query.filter_by(id=self.type_id).first().name,"coordinates":{"latitude":self.latitude,"longitude":self.longitude},
                "images":list(map(lambda image:image.link,self.images)),"contactInfo":User.query.filter_by(id=self.user_id).first().contactInfo() if self.user_id!=None else None
        }
    def add(self):
        db.session.add(self)
        db.session.commit()

