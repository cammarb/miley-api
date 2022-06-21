from flask import Blueprint, jsonify, redirect, url_for
import socket

host = socket. getfqdn()
# addr = socket. gethostbyname(host)
addr = 'miley-api.herokuapp.com'
bp = Blueprint('api', __name__)


@bp.get('/')
def std_index():
    return redirect(url_for('api.index'))


@bp.get('/api/')
@bp.get('/api')
def index():
    return jsonify(
        {
            "songs": addr+"/api/songs",
            "albums": addr+"/api/albums"
        }
    )
