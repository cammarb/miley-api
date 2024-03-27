from uuid import UUID

from app.model.artist import Artist
from app.model.track import Track


def create_track(req_form):
    new_track = Track(
        title=req_form.get("title"),
        slug=req_form.get("slug"),
        length=req_form.get("length"),
        album_id=req_form.get("album_id"),
    )
    new_track.save()

    list_of_artists = req_form.getlist("featuring_artists")
    if list_of_artists:
        for i in range(len(list_of_artists)):
            artist = Artist.query.get(list_of_artists[i])
            new_track.track_artist.append(artist)
            new_track.save()


def edit_track(req_form, id):
    track = Track.query.get(id)
    track.title = req_form.get("title")
    track.slug = req_form.get("slug")
    track.album_id = UUID(req_form.get("album_id"))
    track.length = req_form.get("length")
    track.save()

    list_of_artists = req_form.getlist("featuring_artists")
    if list_of_artists:
        for i in range(len(list_of_artists)):
            artist = Artist.query.get(list_of_artists[i])
            track.track_artist.append(artist)
            track.save()


def delete(id):
    track = Track.query.get(id)
    track.delete()
