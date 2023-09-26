from app.model.users import User
from flask import Blueprint, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.controller.main import get_all, get_one
from app.controller.auth import *

blueprint = Blueprint("auth", __name__)


@blueprint.get("/register")
def get_register():
    return render_template("auth/register.html")


@blueprint.post("/register")
def post_register():
    try:
        register(request.form)
        return redirect(url_for("auth.get_login"))

    except Exception as error_message:
        error = (
            error_message
            or "An error occurred while creating a user. Please make sure to enter valid data."
        )
        return render_template("auth/register.html", error=error)


@blueprint.get("/login")
def get_login():
    return render_template("auth/login.html")


@blueprint.post("/login")
def post_login():
    try:
        login(request.form)
        return redirect(url_for("static_pages.home"))

    except Exception as error_message:
        error = (
            error_message
            or "An error occurred while logging in. Please verify your email and password."
        )
        return render_template("auth/login.html", error=error)


@blueprint.get("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.get_login"))
