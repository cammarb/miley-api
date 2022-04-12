from flask import Blueprint, jsonify
import socket

host = socket. getfqdn()
addr = socket. gethostbyname(host)
bp = Blueprint('api', __name__)


@bp.get('/api/')
@bp.get('/api')
def index():
    return jsonify(
        {
            "songs": addr+"/api/songs",
            "albums": addr+"/api/albums"
        }
    )
