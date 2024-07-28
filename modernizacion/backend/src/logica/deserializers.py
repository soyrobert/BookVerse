import datetime
from marshmallow import Schema, fields, validate, ValidationError

class CreateLibroSchema(Schema):
    titulo = fields.String(
        required=True,
        validate=validate.Regexp(r"^[a-zA-Z0-9]*$"),
        error_messages={"invalid": "Titulo Invalido"},
    )
    fechaPublicacion = fields.DateTime(
        error_messages={"invalid": "fecha Invalida"},
    )
    paginas = fields.Integer(required = True)
    editorial = fields.String(
        required=True,
        validate=validate.Regexp(r"^[a-zA-Z0-9]*$"),
        error_messages={"invalid": "Editorial Invalido"},
    )
    portada = fields.String(
        required=True,
    )

create_schema = CreateLibroSchema()

