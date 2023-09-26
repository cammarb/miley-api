from app.model.users import User
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash


def register(req_form):
    if req_form.get("password") != req_form.get("password_confirmation"):
        raise Exception("The password confirmation must match the password.")
    elif User.query.filter_by(email=req_form.get("email")).first():
        raise Exception("The email address is already registered.")
    else:
        new_user = User(
            name=req_form["name"],
            email=req_form["email"],
            username=req_form["email"].split("@")[0],
            passwd=generate_password_hash(req_form["password"]),
        )
        new_user.save()
        login_user(new_user)


def login(req_form):
    user = User.query.filter_by(email=req_form["email"]).first()
    if not user:
        raise Exception("No user with the given email address was found.")
    elif check_password_hash(req_form["password"], user.passwd):
        raise Exception("Incorrect password.")
    else:
        login_user(user)
