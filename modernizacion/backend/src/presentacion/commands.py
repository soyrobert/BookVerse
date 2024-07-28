from http import HTTPStatus
from flask import Blueprint, jsonify, request, Response
from ..modelos import db, Libro, create_schema
from ..logica.libro_service import LibroService
from marshmallow import ValidationError

operations_command_bp: Blueprint = Blueprint("commands", __name__)
operations_command_prefix: str = "/libros/commands"

@operations_command_bp.route("", methods=["POST"])
def create() -> Response:
    payload = request.get_json()
    try:
        validated_data = create_schema.load(payload)
        libro_service = LibroService()
        libro_service.create_libro(validated_data)
        return {}, HTTPStatus.CREATED.value
    except ValidationError as err:
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST.value
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR.value
