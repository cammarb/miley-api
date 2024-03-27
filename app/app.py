from flask import Flask

from app.extensions.database import db, migrate
from app.extensions.auth import login_manager

from . import view
from app.api.v1 import api


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")

    register_blueprints(app)
    register_extensions(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(view.tracks.blueprint)
    app.register_blueprint(view.albums.blueprint)
    app.register_blueprint(view.static_pages.blueprint)
    app.register_blueprint(view.auth.blueprint)
    # app.register_blueprint(api.blueprint, url_prefix="/api/v1/")


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    login_manager.init_app(app)
