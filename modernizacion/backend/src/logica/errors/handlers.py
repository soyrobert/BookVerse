from .errors import BaseAPIError

from flask import Response
from http import HTTPStatus
from marshmallow import ValidationError


def handle_api_custom_exception(error: BaseAPIError) -> Response:
    """
    Funtion for handling API from request processing.

    Args:
        error (BaseAPIError): Custom API error to handle

    Returns:
        Response: HTTP response with corresponding API status code
    """
    return Response(status=error.code)


def handle_validation_error(error: ValidationError) -> Response:
    """
    Funtion for handling schema validation errors

    Args:
        error (ValidationError): Schema validation error

    Returns:
        Response: HTTP response with corresponding API status code
    """
    return Response(status=HTTPStatus.BAD_REQUEST.value)
