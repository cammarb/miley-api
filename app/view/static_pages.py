from flask import Blueprint, render_template, request


blueprint = Blueprint("static_pages", __name__)


@blueprint.get("/")
def home():
    return render_template("home.html"), request.url_root
