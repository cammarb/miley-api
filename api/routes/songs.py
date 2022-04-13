import json
from flask import Blueprint
from api.models.songs import Song
from api.serializer.serializer import serialize_songs

bp = Blueprint('songs', __name__)


@bp.get('/api/songs/')
@bp.get('/api/songs')
def get_songs():
    songs = Song.query.all()
    return json.dumps(serialize_songs(songs, 0))


@bp.get('/api/songs/<int:id>/')
@bp.get('/api/songs/<int:id>')
def song(id):
    song_id = Song.query.get(id)
    songs = Song.query.all()
    return json.dumps(
        serialize_songs(songs, song_id)
    )
