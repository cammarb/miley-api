import os
from flask import Flask
from app.extensions.database import db, migrate

from . import routes


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_blueprints(app)
    register_extensions(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(routes.api.bp, url_prefix="/api/v1/")


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
