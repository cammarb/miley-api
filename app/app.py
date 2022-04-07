import os
from flask import Flask

from . import api
from . import static_pages


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(static_pages.routes.bp)
    app.register_blueprint(api.routes.bp)
