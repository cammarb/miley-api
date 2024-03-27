from flask import redirect, request, url_for, render_template
from flask import Blueprint
from flask_login import login_required
from app.model.album import Album
from app.controller.main import get_all, get_one
from app.controller.albums import create_album, edit

blueprint = Blueprint("albums", __name__)


# Getting all albums and list them
@blueprint.get("/albums")
def get_albums():
    albums = get_all(Album)
    return render_template("albums/list_albums.html", albums=albums)


@blueprint.get("/albums/add_album")
@login_required
def new_album():
    return render_template("albums/add_album.html")


@blueprint.post("/albums/add_album")
@login_required
def post_album():
    create_album(request.form)
    return redirect(url_for("albums.get_albums"))


@blueprint.get("/albums/<uuid:id>")
@login_required
def get_album(id):
    album = get_one(Album, id)
    return render_template("albums/album.html", album=album)


@blueprint.post("/albums/<uuid:id>/edit")
@login_required
def edit_album(id):
    edit(request.form, id)
    return redirect(url_for("albums.get_albums"))


# Delete a single album
@blueprint.post("/albums/<uuid:id>/delete")
@login_required
def delete_album(id):
    album = get_one(Album, id)
    album.delete()
    return redirect(url_for("albums.get_albums"))
