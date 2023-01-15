from app import app, db
from flask import jsonify
from apifairy import response, body, authenticate, other_responses
from app.schemas import ThingSchema
from app.models import Thing


@app.route("/api/thing/<id>")
@response(ThingSchema)
def get_thing(id):
    """Get a thing from the database"""
    data = Thing.query.get_or_404(id)
    return data


@app.route("/api/thing/", methods=["POST"])
@body(ThingSchema)
@response(ThingSchema)
def create_thing(new_thing):
    """Get a thing from the database"""
    db.session.add(new_thing)
    db.session.commit()

    return new_thing
