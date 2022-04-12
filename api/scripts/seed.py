from api.app import create_app
from api.models.songs import Song
from api.models.albums import Album
from api.models.writers import Writer
from api.models.producers import Producer
from api.models.song_writers import SongWriter
from api.models.song_producers import SongProducer

from api.extensions.database import db

app = create_app()
app.app_context().push()


# Albums
total_songs = 0
tracklist = []

albums = [
    {
        "id": 1,
        "title": "Meet Miley Cyrus",
        "release_date": "2007-06-27",
        "tracklist": tracklist,
        "total_lenght": "33:05"
        # [
        #     "See You Again",
        #     "East Northumberland High",
        #     "Let's Dance",
        #     "G.N.O. (Girl's Night Out)",
        #     "Right Here",
        #     "As I Am",
        #     "Start All Over",
        #     "Clear",
        #     "Good and Broken",
        #     "I Miss You"
        # ],
    }
]

# Songs
songs = [
    {
        "id": "1",
        "title": "See You Again",
        "length": "3:10",
        "album_id": 1
    },
    {
        "id": "2",
        "title": "East Northumberland High",
        "length": "3:24",
        "album_id": 1
    },
    {
        "id": "3",
        "title": "Let's Dance",
        "length": "3:03",
        "album_id": 1
    },
    {
        "id": "4",
        "title": "G.N.O. (Girl's Night Out)",
        "length": "3:38",
        "album_id": 1
    },
    {
        "id": "5",
        "title": "Right Here",
        "length": "2:45",
        "album_id": 1
    },
    {
        "id": "6",
        "title": "As I Am",
        "length": "3:46",
        "album_id": 1
    },
    {
        "id": "7",
        "title": "Start All Over",
        "length": "3:27",
        "album_id": 1
    },
    {
        "id": "8",
        "title": "Clear",
        "length": "3:03",
        "album_id": 1
    },
    {
        "id": "9",
        "title": "Good and Broken",
        "length": "2:56",
        "album_id": 1
    },
    {
        "id": "10",
        "title": "I Miss You",
        "length": "3:58",
        "album_id": 1
    }
]

for song in songs.items():
    new_song = Song(
        id=song['id'],
        title=song['title'],
        length=song['length'],
        album_id=song['album_id']
    )
    db.session.add(new_song)

db.session.commit()

for album in albums.items():
    # song_list = Song.query.all()
    # for song in song_list:
    #     if song['id'] == id:
    #         total_songs = total_songs + 1
    #         tracklist.append(song['title'])
    #     else:
    #         pass

    # for song in songs.items():
    #     if song['id'] == id:
    #         total_songs = total_songs + 1
    #         tracklist.append(song['title'])

    new_album = Album(
        id=album['id'],
        title=album['title'],
        release_date=album['release_date'],
        total_lenght=album['total_lenght'])
    db.session.add(new_album)

db.session.commit()
