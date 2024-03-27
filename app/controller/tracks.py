from uuid import UUID
from app.model.track import Track


def create_track(req_form):
    new_track = Track(
        title=req_form.get("title"),
        slug=req_form.get("slug"),
        length=req_form.get("length"),
        album_id=req_form.get("album_id"),
        featuring_artist=req_form.get("featuring_artist"),
    )
    new_track.save()


def edit_track(req_form, id):
    track = Track.query.get(id)
    track.title = req_form.get("title")
    track.slug = req_form.get("slug")
    track.album_id = UUID(req_form.get("album_id"))
    track.length = req_form.get("length")
    featuring_artist = (req_form.get("featuring_artist"),)
    track.save()


def delete(id):
    track = Track.query.get(id)
    track.delete()
