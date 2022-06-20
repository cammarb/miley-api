from api.models.album import Album
from api.models.song import Song, SongArtist, SongFeaturing
# from api.models.writers import Writer
from api.models.artist import Artist
from datetime import datetime


def serialize_songs(songs, song_id):
    songs_list = []
    artists = Artist.query.all()
    song_artists = SongArtist.query.all()

    for song in songs:
        songs_list.append({
            'id': song.id,
            'title': song.title,
            'slug': song.slug,
            'length': song.length,
            'album': Album.query.get(song.album_id).title,
            'artist': [],
            'featuring': []
        })
        for song_artist in song_artists:
            if artists.song_id == songs_list[(song.id)-1]['id']:
                songs_list[(song.id)-1]['writers'].append(
                    Writer.query.get(song_writer.writer_id).name)
            else:
                pass

    if song_id != 0:
        return songs_list[song_id.id-1]
    else:
        return songs_list


def serialize_albums(albums, album_id):
    albums_list = []
    songs = Song.query.all()

    for album in albums:
        albums_list.append({
            'id': album.id,
            'title': album.title,
            'slug': album.slug,
            'release_date': datetime.strftime(album.release_date, '%Y-%m-%d'),
            'total_length': album.total_length,
            'tracklist': [],
            'total_songs': 0
        })
        for song in songs:
            if song.album_id == albums_list[(album.id)-1]['id']:
                albums_list[(album.id)-1]['tracklist'].append(song.title)
                albums_list[(
                    album.id)-1]['total_songs'] = albums_list[(album.id)-1]['total_songs']+1
            else:
                pass
    if album_id != 0:
        return albums_list[album_id.id-1]
    else:
        return albums_list
