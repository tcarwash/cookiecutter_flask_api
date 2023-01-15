from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from apifairy import APIFairy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object(Config)
apifairy = APIFairy(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)


from app import routes, models, schemas
