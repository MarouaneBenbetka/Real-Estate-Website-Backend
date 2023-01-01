from src.api import db
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(36), primary_key=True, nullable=False, unique=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    annonces = db.relationship("Annonce", backref="owner", lazy=False)
    def toJson(self):
        return {"id" : self.id,"first_name":self.first_name,"last_name":self.last_name,"email":self.email,"phone_number":self.phone_number,"annonces":list(map(lambda annonce:annonce.toJson(),self.annonces))}
    def add(self):
        db.session.add(self)
        db.session.commit()