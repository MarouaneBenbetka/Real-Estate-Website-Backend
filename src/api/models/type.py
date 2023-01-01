from src.api import db
class Type(db.Model):
    __tablename__ = "types"
    id = db.Column(db.Integer, primary_key=True, nullable=True, unique=True)
    name = db.Column(db.String(50), nullable=True)
    annonces = db.relationship("Annonce", backref="annonces", lazy=False)
    def add(self):
        db.session.add(self)
        db.session.commit()