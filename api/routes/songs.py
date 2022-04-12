import json
from flask import Blueprint, jsonify
from datetime import datetime
from api.models.albums import Album
from api.models.songs import Song

bp = Blueprint('api/songs', __name__)


def serialize_songs(songs):
    songs_list = []

    for song in songs:
        songs_list.append({
            'id': song.id,
            'title': song.title,
            'album': Album.query.get(song.album_id).title
        })

    return songs_list


def serialize_song(song):
    song = {
        'id': song.id,
        'title': song.title,
        'album_id': song.album_id
    }

    return song


@bp.get('/songs/')
@bp.get('/songs')
def get_songs():
    songs = Song.query.all()
    return jsonify(serialize_songs(songs))


@bp.get('/songs/<int:id>/')
@bp.get('/songs/<int:id>')
def song(id):
    song = Song.query.get(id)
    return jsonify(
        serialize_song(song)
    )
