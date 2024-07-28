import uuid
import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields
from sqlalchemy.dialects.postgresql import UUID

db: SQLAlchemy = SQLAlchemy()
ma: Marshmallow = Marshmallow()

class Libro(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    titulo = db.Column(db.String(), nullable=False, unique=True)
    fechaPublicacion = db.Column(db.DateTime())
    paginas = db.Column(db.Integer)
    editorial = db.Column(db.String())
    portada = db.Column(db.String())
    createdAt = db.Column(
        db.DateTime(),
        default=datetime.datetime.now(),
    )

class LibroSerializerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Libro
        load_instance = True

    id = fields.String()
    titulo = fields.String()
    fechaPublicacion = fields.DateTime()
    paginas =  fields.Integer()
    editorial = fields.String()
    portada = fields.String()
    createdAt = fields.DateTime(load_only=True)

libro_schema = LibroSerializerSchema()