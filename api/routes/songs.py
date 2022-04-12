import json
from flask import Blueprint, jsonify
from api.models.albums import Album
from api.models.producers import Producer
from api.models.songs import Song
from api.models.song_writers import SongWriter
from api.models.song_producers import SongProducer
from api.models.writers import Writer

bp = Blueprint('songs', __name__)


def serialize_songs(songs):
    songs_list = []

    for song in songs:
        songs_list.append({
            'id': song.id,
            'title': song.title,
            'length': song.length,
            'album': Album.query.get(song.album_id).title,
        })

    return songs_list


def serialize_song(song):
    song_writers = SongWriter.query.all()
    song_producers = SongProducer.query.all()
    song = {
        'id': song.id,
        'title': song.title,
        'album_title': Album.query.get(song.album_id).title,
        'length': song.length,
        'writers': [],
        'producers': []
    }
    for song_writer in song_writers:
        if song_writer.song_id == song['id']:
            song['writers'].append(
                Writer.query.get(song_writer.writer_id).name)

    for song_producer in song_producers:
        if song_producer.song_id == song['id']:
            song['producers'].append(
                Producer.query.get(song_producer.producer_id).name)

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
