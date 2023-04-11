import os
from flask import Flask
from flask_cors import CORS
from api.extensions.database import db, migrate

from . import routes


def create_app():
    app = Flask(__name__)
    app.config.from_object("api.config")

    CORS(app)

    register_blueprints(app)
    register_extensions(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(routes.index.bp)
    app.register_blueprint(routes.albums.bp)
    app.register_blueprint(routes.songs.bp)


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
