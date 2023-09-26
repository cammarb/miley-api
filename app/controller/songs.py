from app.model.album import Album
from app.model.artist import Artist
from app.model.song import Song, SongArtist, SongFeaturing


def create_song(req_form):
    new_song = Song(
        title=req_form.get("title"),
        slug=req_form.get("slug"),
        album_id=req_form.get("album_id"),
        length=req_form.get("length"),
    )
    new_song.save()
    list_of_artists = req_form.getlist("main_artist")
    for i in range(len(list_of_artists)):
        artist = Artist.query.get(list_of_artists[i])
        new_song.song_artist.append(
            artist
        )  # Add to helper table relationship between Song and Artists
        new_song.save()
    featuring_artists = req_form.getlist("ft_artist")
    for i in range(len(featuring_artists)):
        ft_artist = Artist.query.get(featuring_artists[i])
        new_song.song_featuring.append(
            ft_artist
        )  # Add to helper table relationship between Song and Artists
        new_song.save()

    # Everytime you create a song the amount of songs in that album (if present)
    # gets updated by searching all created songs related to that album_id
    if new_song.album_id != None:
        song_album = Album.query.get(new_song.album_id)
        song_album.number_of_songs = Song.query.filter_by(
            album_id=new_song.album_id
        ).count()
        song_album.save()


def edit_song(req_form, id):
    song = Song.query.get(id)
    song.title = req_form.get("title")
    song.slug = req_form.get("slug")
    song.album_id = req_form.get("album_id")
    song.length = req_form.get("length")
    song.save()

    # First we remove the previously added relationships
    list_song_artists = SongArtist.query.filter_by(song_id=id)
    for song_artist in list_song_artists:
        song_artist.delete()
    list_song_featurings = SongFeaturing.query.filter_by(song_id=id)
    for song_featuring in list_song_featurings:
        song_featuring.delete()

    # Then we add the artists selected
    list_of_artists = req_form.getlist("main_artist")
    for i in range(len(list_of_artists)):
        artist = Artist.query.get(list_of_artists[i])
        song.song_artist.append(
            artist
        )  # Add to helper table relationship between Song and Artists
        song.save()
    featuring_artists = req_form.getlist("ft_artist")
    for i in range(len(featuring_artists)):
        ft_artist = Artist.query.get(featuring_artists[i])
        song.song_featuring.append(
            ft_artist
        )  # Add to helper table relationship between Song and Artists
        song.save()


def delete(id):
    song = Song.query.get(id)
    song_album = Album.query.get(song.album_id)
    song.delete()
    song_album.number_of_songs = Song.query.filter_by(album_id=song.album_id).count()
    song_album.save()
