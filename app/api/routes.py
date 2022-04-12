import json
from flask import Blueprint, jsonify
from datetime import datetime
from app.models.albums import Album
from app.models.songs import Song
import socket
host = socket. getfqdn()
addr = socket. gethostbyname(host)
bp = Blueprint('api', __name__)


@bp.get('/api/')
@bp.get('/api')
def index():
    return jsonify({
        "songs": addr+"/api/songs",
        "albums": addr+"/api/albums"})

# Albums


def serialize_albums(albums):
    albums_list = []

    for album in albums:
        albums_list.append({
            'id': album.id,
            'title': album.title,
            'release_date': datetime.strftime(album.release_date, '%Y-%m-%d')
        })

    return albums_list


def serialize_album(album):
    songs = Song.query.all()

    album = {
        'id': album.id,
        'title': album.title,
        'release_date': datetime.strftime(album.release_date, '%Y-%m-%d'),
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

# Songs


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


@bp.get('/api/songs/')
@bp.get('/api/songs')
def get_songs():
    songs = Song.query.all()
    return jsonify(serialize_songs(songs))


@bp.get('/api/songs/<int:id>/')
@bp.get('/api/songs/<int:id>')
def song(id):
    song = Song.query.get(id)
    return jsonify(
        serialize_song(song)
    )
