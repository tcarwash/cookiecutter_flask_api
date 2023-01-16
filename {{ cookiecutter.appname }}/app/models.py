from app import db
import secrets
from datetime import datetime, timedelta

from werkzeug.security import check_password_hash, generate_password_hash


class Thing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thing = db.Column(db.String(64), index=True, unique=True)
    number_thing = db.Column(db.Integer, index=True)
    auto_date_thing = db.Column(db.DateTime, index=True, default=datetime.now())


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hashed = db.Column(db.String(128), nullable=False)
    auth_token = db.Column(db.String(64), index=True)
    auth_token_expiration = db.Column(db.DateTime)

    def __init__(self, email: str, password_plaintext: str):
        """Create a new User"""
        self.email = email
        self.password_hashed = self._generate_password_hash(password_plaintext)

    def is_password_correct(self, password_plaintext: str):
        return check_password_hash(self.password_hashed, password_plaintext)

    def set_password(self, password_plaintext: str):
        self.password_hashed = self._generate_password_hash(password_plaintext)

    @staticmethod
    def _generate_password_hash(password_plaintext):
        return generate_password_hash(password_plaintext)

    def generate_auth_token(self):
        self.auth_token = secrets.token_urlsafe()
        self.auth_token_expiration = datetime.utcnow() + timedelta(minutes=60)
        return self.auth_token

    @staticmethod
    def verify_auth_token(auth_token):
        user = User.query.filter_by(auth_token=auth_token).first()
        if user and user.auth_token_expiration > datetime.utcnow():
            return user

    def revoke_auth_token(self):
        self.auth_token_expiration = datetime.utcnow()

    def __repr__(self):
        return f"<User: {self.email}>"
