import json
from datetime import datetime
import sqlite3
from flask import Flask, Blueprint, jsonify, redirect, render_template, request, url_for
from .models import Album

bp = Blueprint('albums', __name__)


# @bp.get('/albums/all')
# def albums():
#     albums = Album.query.all()
#     return jsonify(serialize_albums(albums))


@bp.get('/albums/add')
def add_albums():
    return render_template('albums/add_album.html')


@bp.post('/albums/add')
def post_albums():
    new_album = Album(
        title=request.form['title'],
        release_date=datetime.strptime(
            request.form['release_date'], '%Y-%m-%d')
    )
    new_album.save()
    return redirect(url_for('albums.album', id=new_album.id))


@bp.get('/albums/<id>')
def album(id):
    album = Album.query.get(id)
    return f'''ID: {str(album.id)}
    title: {album.title}
    date: {str(album.release_date)}'''
