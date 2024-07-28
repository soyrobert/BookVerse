import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .modelos.libro import db, Libro

def create_app():
    app = Flask(__name__)
    
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

with app.app_context():
    db.create_all()
    print("Tablas creadas exitosamente.")
