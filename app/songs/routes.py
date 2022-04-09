from .models import Song
from app.albums.models import Album
from flask import Blueprint, redirect, render_template, request, url_for

bp = Blueprint('songs', __name__)


@bp.get('/songs/add')
def add_song():
    albums = Album.query.all()
    return render_template('songs/add_song.html', albums=albums)


@bp.post('/songs/add')
def post_song():

    new_song = Song(
        title=request.form['title'],
        album_id=request.form['album_id']
    )
    new_song.save()
    return redirect(url_for('songs.song', id=new_song.id))


@bp.get('/songs/<id>')
def song(id):
    song = Song.query.get(id)
    return f'''
    id: {song.id}
    album_id: {song.album_id}
    title: {song.title}
    '''


@bp.get('/songs/all')
def all_songs():
    return render_template('songs/all_songs.html')
