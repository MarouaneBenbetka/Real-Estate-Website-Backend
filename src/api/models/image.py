from src.api import db
class Image(db.Model):
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key=True, nullable=True, unique=True)
    link = db.Column(db.String(255), nullable=True)
    annonce_id = db.Column(db.String(36), db.ForeignKey("annonces.id"))
    def toJson(self):
        return {"imageLink":self.link}
    def add(self):
        db.session.add(self)
        db.session.commit()