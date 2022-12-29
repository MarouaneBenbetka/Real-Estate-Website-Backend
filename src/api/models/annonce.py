from api import db
class Annonce(db.Model):
    __tablename__ = "annonces"
    id = db.Column(db.String(36), primary_key=True, nullable=False, unique=True)
    category = db.Column(db.String(1), nullable=False)
    surface = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    wilaya_num = db.Column(db.String(2),nullable=False)
    commune = db.Column(db.String(30),nullable=False)
    address = db.Column(db.String(50),nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"))
    type_id = db.Column(db.Integer, db.ForeignKey("types.id"))
    images = db.relationship("Image", backref="annonce", lazy=False)
