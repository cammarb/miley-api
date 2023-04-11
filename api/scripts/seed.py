import datetime
from api.app import create_app
from api.models.song import Song
from api.models.album import Album

from api.extensions.database import db

app = create_app()
app.app_context().push()


# Albums
albums = [
    {
        "id": 1,
        "title": "Meet Miley Cyrus",
        "slug": "meet-miley-cyrus",
        "release_date": datetime.date(2007, 6, 27),
        "total_length": "33:05",
    }
]

# Songs
songs = [
    {
        "id": "1",
        "title": "See You Again",
        "slug": "see-you-again",
        "length": "3:10",
        "album_id": 1,
    },
    {
        "id": "2",
        "title": "East Northumberland High",
        "slug": "east-northumberland-high",
        "length": "3:24",
        "album_id": 1,
    },
    {
        "id": "3",
        "title": "Let's Dance",
        "slug": "lets-dance",
        "length": "3:03",
        "album_id": 1,
    },
    {
        "id": "4",
        "title": "G.N.O. (Girl's Night Out)",
        "slug": "gno-girls-night-out",
        "length": "3:38",
        "album_id": 1,
    },
    {
        "id": "5",
        "title": "Right Here",
        "slug": "right-here",
        "length": "2:45",
        "album_id": 1,
    },
    {"id": "6", "title": "As I Am", "slug": "as-i-am", "length": "3:46", "album_id": 1},
    {
        "id": "7",
        "title": "Start All Over",
        "slug": "start-all-over",
        "length": "3:27",
        "album_id": 1,
    },
    {"id": "8", "title": "Clear", "slug": "clear", "length": "3:03", "album_id": 1},
    {
        "id": "9",
        "title": "Good and Broken",
        "slug": "good-and-broken",
        "length": "2:56",
        "album_id": 1,
    },
    {
        "id": "10",
        "title": "I Miss You",
        "slug": "i-miss-you",
        "length": "3:58",
        "album_id": 1,
    },
]

for song in songs:
    new_song = Song(
        id=song["id"],
        title=song["title"],
        slug=song["slug"],
        length=song["length"],
        album_id=song["album_id"],
    )
    db.session.add(new_song)

db.session.commit()

for album in albums:
    new_album = Album(
        id=album["id"],
        title=album["title"],
        slug=album["slug"],
        release_date=album["release_date"],
        total_length=album["total_length"],
    )
    db.session.add(new_album)

db.session.commit()
