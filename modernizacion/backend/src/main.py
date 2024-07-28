import os
from flask import Flask, jsonify
from .presentacion import operations_command_bp, operations_command_prefix, operations_query_prefix, operations_query_bp
from .modelos import db, ma
from .logica import BaseAPIError, handle_validation_error, handle_api_custom_exception
from .utils import DatabaseUtil
import awsgi
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

def create_app():
    """
    Factory function for generating a new application

    Returns:
        flask.Flask: application instance
    """
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DatabaseUtil.generate_database_uri()

    with app.app_context():
        db.init_app(app=app)
        ma.init_app(app=app)
        db.create_all()

    app.register_blueprint(operations_command_bp, url_prefix=operations_command_prefix)
    app.register_blueprint(operations_query_bp, url_prefix=operations_query_prefix)
    app.register_error_handler(BaseAPIError, handle_api_custom_exception)

    @app.route("/health")
    def health():
        return jsonify({"status": "healthy"})

    CORS(app)

    return app

app = create_app()

@app.route('/')
def index():
    return jsonify(status=200, message='OK')

@app.route('/initialize')
def initialize_db():
    with app.app_context():
        db.create_all()
        return jsonify(status=200, message="Tablas creadas exitosamente.")

if __name__ == "__main__":
    app.run()

def lambda_handler(event, context):
    return awsgi.response(app, event, context)
