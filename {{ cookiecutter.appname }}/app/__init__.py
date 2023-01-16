from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from apifairy import APIFairy
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object(Config)
apifairy = APIFairy(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()
migrate = Migrate(app, db)


from app import routes, models, schemas, auth
