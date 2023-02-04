from src.api import db


class ContactInfo(db.Model):
    __tablename__ = "contactInfos"
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    phone_number = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(255))
    user = db.relationship("User", backref="info", lazy=False)
    annonces = db.relationship("Annonce", backref="contactInfo", lazy=False)
    full_name = db.Column(db.String(30))

    def toJson(self):
        return {"name": self.full_name, "email": self.email, "phoneNumber": self.phone_number, "address": self.address}

    def add(self):
        db.session.add(self)
        db.session.commit()
