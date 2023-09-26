from app.model.album import Album
from datetime import datetime


def create_album(req_form):
    new_album = Album(
        title=req_form.get("title"),
        slug=req_form.get("slug"),
        release_date=datetime.strptime(req_form.get("release_date"), "%Y-%m-%d"),
        is_live=req_form.get("is_live"),
        is_ep=req_form.get("is_ep"),
        number_of_songs=0,
        total_length=req_form.get("total_length"),
        artist_id=req_form.get("artist_id"),
    )
    new_album.save()


def edit(req_form, id):
    album = Album.query.get(id)
    album.title = req_form.get("title")
    album.slug = req_form.get("slug")
    album.release_date = datetime.strptime(req_form.get("release_date"), "%Y-%m-%d")
    album.is_live = req_form.get("is_live")
    album.is_ep = req_form.get("is_ep")
    # album.number_of_songs doesn't change when we edit the album
    album.total_length = req_form.get("total_length")
    album.artist_id = req_form.get("artist_id")
    album.save()
