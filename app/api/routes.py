import json
from datetime import datetime
import sqlite3
from flask import Blueprint, jsonify
from app.albums.models import Album
from app.songs.models import Song

bp = Blueprint('api', __name__)

# Albums


def serialize_albums(albums):
    albums_list = []

    for album in albums:
        albums_list.append({
            'id': album.id,
            'title': album.title,
            'release_date': album.release_date
        })

    return albums_list


def serialize_album(album):
    album = {
        'id': album.id,
        'title': album.title,
        'release_date': album.release_date
    }

    return album


@bp.get('/api/v1/albums')
def get_albums():
    albums = Album.query.all()
    return jsonify(serialize_albums(albums))


@bp.get('/api/v1/albums/<int: id>')
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
            'album_id': song.album_id
        })

    return songs_list


def serialize_song(song):
    song = {
        'id': song.id,
        'title': song.title,
        'album_id': song.album_id
    }

    return song


@bp.get('/api/v1/songs')
def get_songs():
    songs = Song.query.all()
    albums = Album.query.all()
    return jsonify(serialize_songs(songs))


@bp.get('/api/v1/songs/<int: id>')
def song(id):
    song = Song.query.get(id)
    return jsonify(
        serialize_song(song)
    )
