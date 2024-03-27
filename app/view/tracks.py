from flask import redirect, request, render_template, url_for, abort
from flask import Blueprint
from flask_login import login_required

from app.model.track import Track
from app.model.album import Album
from flask_sqlalchemy import SQLAlchemy
from app.controller.main import get_all, get_one
from app.controller.tracks import create_track, edit_track, delete

dbb = SQLAlchemy()

blueprint = Blueprint("tracks", __name__)


@blueprint.get("/tracks")
def get_tracks():
    tracks = get_all(Track)
    albums = get_all(Album)

    return render_template(
        "tracks/list_tracks.html",
        tracks=tracks,
        albums=albums,
    )


@blueprint.get("/tracks/<uuid:id>")
def get_track(id):
    track = get_one(Track, id)
    if track is None:
        abort(404)

    albums = get_all(Album)

    return render_template(
        "tracks/track.html",
        track=track,
        albums=albums,
    )


@blueprint.post("/tracks/<uuid:id>/edit")
def update_track(id):
    edit_track(request.form, id)
    return redirect(url_for("tracks.get_tracks"))


@blueprint.post("/tracks/<uuid:id>/delete")
@login_required
def delete_track(id):
    delete(id)
    return redirect(url_for("tracks.get_tracks"))


@blueprint.get("/tracks/add_song")
@login_required
def add_track():
    albums = get_all(Album)
    return render_template("tracks/add_track.html", albums=albums)


@blueprint.post("/tracks/add_song")
@login_required
def post_track():
    create_track(request.form)
    return redirect(url_for("tracks.get_tracks"))
