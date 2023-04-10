from flask import Blueprint, jsonify, redirect, request, url_for
import socket

host = socket.getfqdn()
# addr = socket. gethostbyname(host)
# addr =
bp = Blueprint("api", __name__)


@bp.get("/")
def std_index():
    return redirect(url_for("api.index"))


@bp.get("/api/")
@bp.get("/api")
def index():
    return jsonify(
        {
            "songs": request.url_root + "api/songs",
            "albums": request.url_root + "api/albums",
        }
    )
