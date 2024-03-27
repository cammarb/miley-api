from flask import redirect, request, render_template, url_for, abort
from flask import Blueprint
from flask_login import login_required
from collections import defaultdict
from uuid import UUID

from app.model.track import Track
from app.model.artist import Artist, TrackArtist
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
    artists = get_all(Artist)
    featuring_artists = get_all(TrackArtist)

    track_artist_mapping = defaultdict(list)
    for feat_artist in featuring_artists:
        track_artist_mapping[feat_artist.track_id].append(
            next(
                artist.name for artist in artists if artist.id == feat_artist.artist_id
            )
        )

    return render_template(
        "tracks/list_tracks.html",
        tracks=tracks,
        albums=albums,
        track_artist_mapping=track_artist_mapping,
    )


@blueprint.get("/tracks/<uuid:id>")
def get_track(id):
    track = get_one(Track, id)
    if track is None:
        abort(404)

    albums = get_all(Album)
    artists = get_all(Artist)
    track_artists = TrackArtist.query.filter_by(track_id=id).all()
    artist_ids = [track_artist.artist_id for track_artist in track_artists]
    featuring_artists = Artist.query.filter(Artist.id.in_(artist_ids)).all()

    return render_template(
        "tracks/track.html",
        track=track,
        albums=albums,
        featuring_artists=featuring_artists,
        artists=artists,
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
    artists = get_all(Artist)
    return render_template("tracks/add_track.html", albums=albums, artists=artists)


@blueprint.post("/tracks/add_song")
@login_required
def post_track():
    create_track(request.form)
    return redirect(url_for("tracks.get_tracks"))
