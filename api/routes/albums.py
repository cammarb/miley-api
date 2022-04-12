import json
from flask import Blueprint, jsonify
from datetime import datetime
from api.models.albums import Album
from api.models.songs import Song

bp = Blueprint('albums', __name__)


def serialize_albums(albums):
    albums_list = []

    for album in albums:
        albums_list.append({
            'id': album.id,
            'title': album.title,
            'release_date': datetime.strftime(album.release_date, '%Y-%m-%d'),
            'total_length': album.total_length,
        })

    return albums_list


def serialize_album(album):
    songs = Song.query.all()

    album = {
        'id': album.id,
        'title': album.title,
        'release_date': datetime.strftime(album.release_date, '%Y-%m-%d'),
        'total_length': album.total_length,
        'tracklist': []
    }
    for song in songs:
        if song.album_id == album['id']:
            album['tracklist'].append(song.title)

    return album


@bp.get('/api/albums/')
@bp.get('/api/albums')
def get_albums():
    albums = Album.query.all()
    return jsonify(serialize_albums(albums))


@bp.get('/api/albums/<int:id>/')
@bp.get('/api/albums/<int:id>')
def album(id):
    album = Album.query.get(id)
    return jsonify(
        serialize_album(album)
    )
