from app import ma
from app.models import Thing


class ThingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Thing
        load_instance = True

    id = ma.auto_field(dump_only=True)
    auto_date_thing = ma.auto_field(dump_only=True)
