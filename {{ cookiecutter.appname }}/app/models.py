from app import db
from datetime import datetime


class Thing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thing = db.Column(db.String(64), index=True, unique=True)
    number_thing = db.Column(db.Integer, index=True)
    auto_date_thing = db.Column(db.DateTime, index=True, default=datetime.now())
