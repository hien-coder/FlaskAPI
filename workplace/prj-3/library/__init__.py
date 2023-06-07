from flask import Flask
from flask_cors import CORS
from .extension import db
from .model import *

def create_db(app):
    db.init_app(app)
    
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    CORS(app)

    create_db(app)

    return app
