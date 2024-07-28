from http import HTTPStatus
from flask import Blueprint, jsonify, request, Response
from ..logica.deserializers import create_schema
from ..logica.libro_service import LibroService
from ..modelos import db, Libro, libro_schema

operations_query_bp: Blueprint = Blueprint("queries", __name__)
operations_query_prefix: str = "/libros/queries"

@operations_query_bp.route("", methods=["GET"])
def obtener_libros() -> Response:
    try:
        libro_service = LibroService()
        libros = libro_service.obtener_libros()

        return libros, HTTPStatus.OK
    except ValueError:
        return "", 400
    except Exception as ex:
        return {"error": str(ex)}, 500
    