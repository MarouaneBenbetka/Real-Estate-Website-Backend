from src.api import db
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(36), primary_key=True, nullable=False, unique=True)
    full_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    picture_link = db.Column(db.String(255))
    contact_info_id = db.Column(db.Integer,db.ForeignKey("contactInfos.id"))
    annonces = db.relationship("Annonce", backref="owner", lazy="dynamic")
    role = db.Column(db.String(1),default="1")
    def toJson(self):
        return {"id" : self.id,"full_name":self.full_name,"email":self.email,"phone_number":self.info.phone_number,"annonces":list(map(lambda annonce:annonce.toJson(),self.annonces))}
    def add(self):
        db.session.add(self)
        db.session.commit()