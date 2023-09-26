from flask import redirect, request, render_template, url_for
from flask import Blueprint
from flask_login import login_required
from app.model.song import Song, SongArtist, SongFeaturing
from app.model.artist import Artist
from app.model.album import Album
from flask_sqlalchemy import SQLAlchemy
from app.controller.main import get_all, get_one
from app.controller.songs import create_song, edit_song, delete

dbb = SQLAlchemy()

blueprint = Blueprint("songs", __name__)


@blueprint.get("/songs")
def get_songs():
    songs = get_all(Song)
    albums = get_all(Album)
    return render_template("songs/list_songs.html", songs=songs, albums=albums)


@blueprint.get("/songs/<int:id>")
@login_required
def get_song(id):
    song = get_one(Song, id)
    song_artists = SongArtist.query.filter_by(song_id=id)
    song_featurings = SongFeaturing.query.filter_by(song_id=id)
    albums = get_all(Album)
    artists = get_all(Artist)
    return render_template(
        "songs/song.html",
        song=song,
        albums=albums,
        artists=artists,
        song_artists=song_artists,
        song_featurings=song_featurings,
    )


@blueprint.post("/songs/<int:id>/edit")
@login_required
def update_song(id):
    edit_song(request.form, id)
    return redirect(url_for("songs.get_songs"))


@blueprint.post("/songs/<int:id>/delete")
@login_required
def delete_song(id):
    delete(id)
    return redirect(url_for("songs.get_songs"))


@blueprint.get("/songs/add_song")
@login_required
def add_song():
    albums = get_all(Album)
    artists = get_all(Artist)
    return render_template("songs/add_song.html", albums=albums, artists=artists)


@blueprint.post("/songs/add_song")
@login_required
def post_song():
    create_song(request.form)
    return redirect(url_for("songs.get_songs"))
