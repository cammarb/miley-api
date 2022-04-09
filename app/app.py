import os
from flask import Flask
from app.extensions.database import db, migrate

from . import api
from . import static_pages
from . import songs
from . import albums


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_blueprints(app)
    register_extensions(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(static_pages.routes.bp)
    app.register_blueprint(api.routes.bp)
    app.register_blueprint(albums.routes.bp)
    app.register_blueprint(songs.routes.bp)


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
