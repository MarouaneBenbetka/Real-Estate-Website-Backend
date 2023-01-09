from src.api import db
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(36), primary_key=True, nullable=False, unique=True)
    full_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(10))
    address = db.Column(db.String(50))
    picture_link = db.Column(db.String(255))
    annonces = db.relationship("Annonce", backref="owner", lazy=False)
    def toJson(self):
        return {"id" : self.id,"full_name":self.full_name,"email":self.email,"phone_number":self.phone_number,"annonces":list(map(lambda annonce:annonce.toJson(),self.annonces))}
    def contactInfo(self):
        return {"id" : self.id,"name":self.full_name,"email":self.email,"phoneNumber":self.phone_number,"address":self.address,"picture":self.picture_link}
    def add(self):
        db.session.add(self)
        db.session.commit()