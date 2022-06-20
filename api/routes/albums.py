import json
from flask import Blueprint, jsonify
from api.models.album import Album
from api.serializer.serializer import serialize_albums

bp = Blueprint('albums', __name__)


@bp.get('/api/albums/')
@bp.get('/api/albums')
def get_albums():
    albums = Album.query.all()
    return jsonify(
        serialize_albums(albums, 0)
    )


# @bp.get('/api/albums/<int:id>/')
# @bp.get('/api/albums/<int:id>')
# def album(id):
#     albums = Album.query.all()
#     album_id = Album.query.get(id)
#     return json.dumps(
#         serialize_albums(albums, album_id)
#     )
