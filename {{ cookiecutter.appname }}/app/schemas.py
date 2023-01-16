from app import ma
from app.models import Thing


class ThingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Thing
        load_instance = True

    id = ma.auto_field(dump_only=True)
    auto_date_thing = ma.auto_field(dump_only=True)


class NewUserSchema(ma.Schema):
    """Schema defining the attributes required for creating a user"""

    email = ma.String()
    password_plaintext = ma.String()


class UserSchema(ma.Schema):
    """Schema defining the attributes of a user."""

    id = ma.Integer()
    email = ma.String()


class TokenSchema(ma.Schema):
    """Schema defining the attributes of a token"""

    token = ma.String()


new_user_schema = NewUserSchema()
user_schema = UserSchema()
token_schema = TokenSchema()
