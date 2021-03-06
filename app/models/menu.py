from app import db
from datetime import datetime

class Menu(db.Model):
    """ Menu model for storing menu related data """
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), index=True)
    name = db.Column(db.String(64))
    price = db.Column(db.Float)
    description = db.Column(db.String(256))
    image = db.Column(db.String(128))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    orders = db.relationship('Order', backref='menu', lazy='dynamic')

    def __repr__(self) -> str:
        return '<Menus Restaurant id {}>'.format(self.restaurant_id)