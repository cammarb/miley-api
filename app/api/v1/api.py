# from flask import Blueprint, jsonify, request, abort
# import socket

# from app.model.album import Album
# from app.model.song import Song

# from .serializer import *

# blueprint = Blueprint("api", __name__)


# @blueprint.errorhandler(404)
# def resource_not_found(e):
#     return jsonify(error=str(e))


# @blueprint.get("/")
# def index():
#     return jsonify(
#         {
#             "songs": request.url_root + "api/v1/songs",
#             "albums": request.url_root + "api/v1/albums",
#         }
#     )


# @blueprint.get("/albums")
# def get_albums():
#     albums = Album.query.all()
#     return jsonify(serialize_albums(albums, 0))


# @blueprint.get("/albums/<int:id>")
# def album(id):
#     albums = Album.query.all()
#     album_id = Album.query.get(id)
#     if album_id is None:
#         abort(404, description="Album not found")
#     return jsonify(serialize_albums(albums, album_id))


# @blueprint.get("/songs")
# def get_songs():
#     songs = Song.query.all()
#     return jsonify(serialize_songs(songs, 0))


# @blueprint.get("/songs/<int:id>")
# def song(id):
#     songs = Song.query.all()
#     song_id = Song.query.get(id)

#     if song_id is None:
#         abort(404, description="Song not found")
#     return jsonify(serialize_songs(songs, song_id))
