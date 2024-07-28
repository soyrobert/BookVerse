from http import HTTPStatus
from flask import Blueprint, jsonify, request, Response
from ..logica.deserializers import create_schema
from ..logica.libro_service import LibroService
from ..modelos import db, Libro, libro_schema

operations_command_bp: Blueprint = Blueprint("commands", __name__)
operations_command_prefix: str = "/libros/commands"

@operations_command_bp.route("", methods=["POST"])
def create() -> Response:
    payload = request.get_json()
    print(payload)
    validated_data = create_schema.load(payload)
    print(validated_data)
    libro_service = LibroService()
    libro_service.create_libro(validated_data)

    return {}, HTTPStatus.CREATED.value
    