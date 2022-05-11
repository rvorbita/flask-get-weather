from app import db
from datetime import datetime

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, index=True, default=datetime.now())

    def __repr__(self):

        return f'city: {self.name}'