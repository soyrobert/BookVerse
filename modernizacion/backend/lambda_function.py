import os
from flask import Flask, jsonify
from src.modelos.libro import db, Libro
from src.utils.database import DatabaseUtil
import awsgi
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    database_uri = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

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
