from app import app, db, basic_auth
from flask import jsonify
from apifairy import response, body, authenticate, other_responses
from app.schemas import ThingSchema, user_schema, token_schema, new_user_schema
from app.models import Thing, User

### Authentication


@app.route("/api/users", methods=["POST"])
@body(new_user_schema)
@response(user_schema, 201)
def register(kwargs):
    """Create a new user"""
    new_user = User(**kwargs)
    db.session.add(new_user)
    db.session.commit()
    return new_user


@app.route("/api/users/get-auth-token", methods=["POST"])
@authenticate(basic_auth)
@response(token_schema)
@other_responses({401: "Invalid username or password"})
def get_auth_token():
    """Get authentication token"""
    user = basic_auth.current_user()
    token = user.generate_auth_token()
    db.session.add(user)
    db.session.commit()
    return dict(token=token)


### Main routes


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
    """Create a thing in the database"""
    db.session.add(new_thing)
    db.session.commit()

    return new_thing
