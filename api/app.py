import os
from flask import Flask
from flask_cors import CORS
from api.extensions.database import db, migrate

from . import views


def create_app():
    app = Flask(__name__)
    app.config.from_object("api.config")

    CORS(app)

    register_blueprints(app)
    register_extensions(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(views.index.bp)
    app.register_blueprint(views.albums.bp)
    app.register_blueprint(views.songs.bp)


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
