import datetime
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
albums = [
    {
        "id": 1,
        "title": "Meet Miley Cyrus",
        "release_date": datetime.date(2007, 6, 27),
        "total_length": "33:05"
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

writers = [
    {
        "id": 1,
        "name": "Destiny Hope Cyrus"
    },
    {
        "id": 2,
        "name": "Armato"
    },
    {
        "id": 3,
        "name": "James"
    },
    {
        "id": 4,
        "name": "Samantha Jo Moore"
    },
    {
        "id": 5,
        "name": "Matthew Wilder"
    },
    {
        "id": 6,
        "name": "Tamara Dunn"
    },
    {
        "id": 7,
        "name": "Shelley Peiken"
    },
    {
        "id": 8,
        "name": "Xandy Barry"
    },
    {
        "id": 9,
        "name": "Scott Cutler"
    },
    {
        "id": 10,
        "name": "Anne Preven"
    },
    {
        "id": 11,
        "name": "Fefe Dobson"
    },
    {
        "id": 12,
        "name": "Peiken"
    },
    {
        "id": 13,
        "name": "Brian Green"
    },
    {
        "id": 14,
        "name": "Wendi Foy Green"
    }
]


producers = [
    {
        "id": 1,
        "name": "Armato"
    },
    {
        "id": 2,
        "name": "James"
    },
    {
        "id": 3,
        "name": "Wilder"
    },
    {
        "id": 4,
        "name": "Xandy Barry"
    },
    {
        "id": 5,
        "name": "Wally Gagel"
    },
    {
        "id": 6,
        "name": "Annetenna"
    },
    {
        "id": 7,
        "name": "Brian Green"
    }
]

song_writers = [
    {
        "song_id": 1,
        "writer_id": 1
    },
    {
        "song_id": 1,
        "writer_id": 2
    },
    {
        "song_id": 1,
        "writer_id": 3
    },
    {
        "song_id": 2,
        "writer_id": 2
    },
    {
        "song_id": 2,
        "writer_id": 3
    },
    {
        "song_id": 2,
        "writer_id": 4
    },
    {
        "song_id": 3,
        "writer_id": 1
    },
    {
        "song_id": 3,
        "writer_id": 2
    },
    {
        "song_id": 3,
        "writer_id": 3
    },
    {
        "song_id": 4,
        "writer_id": 1
    },
    {
        "song_id": 4,
        "writer_id": 5
    },
    {
        "song_id": 4,
        "writer_id": 6
    },
    {
        "song_id": 5,
        "writer_id": 1
    },
    {
        "song_id": 5,
        "writer_id": 2
    },
    {
        "song_id": 5,
        "writer_id": 3
    },
    {
        "song_id": 6,
        "writer_id": 1
    },
    {
        "song_id": 6,
        "writer_id": 7
    },
    {
        "song_id": 6,
        "writer_id": 8
    },
    {
        "song_id": 7,
        "writer_id": 9
    },
    {
        "song_id": 7,
        "writer_id": 10
    },
    {
        "song_id": 7,
        "writer_id": 11
    },
    {
        "song_id": 8,
        "writer_id": 1
    },
    {
        "song_id": 8,
        "writer_id": 12
    },
    {
        "song_id": 8,
        "writer_id": 8
    },
    {
        "song_id": 9,
        "writer_id": 1
    },
    {
        "song_id": 9,
        "writer_id": 2
    },
    {
        "song_id": 9,
        "writer_id": 3
    },
    {
        "song_id": 10,
        "writer_id": 1
    },
    {
        "song_id": 10,
        "writer_id": 13
    },
    {
        "song_id": 10,
        "writer_id": 14
    }
]

song_producers = [
    {
        "song_id": 1,
        "producer_id": 2
    },
    {
        "song_id": 1,
        "producer_id": 3
    },
    {
        "song_id": 2,
        "producer_id": 2
    },
    {
        "song_id": 2,
        "producer_id": 3
    },
    {
        "song_id": 3,
        "producer_id": 2
    },
    {
        "song_id": 3,
        "producer_id": 3
    },
    {
        "song_id": 4,
        "producer_id": 5
    },
    {
        "song_id": 5,
        "producer_id": 2
    },
    {
        "song_id": 5,
        "producer_id": 3
    },
    {
        "song_id": 6,
        "producer_id": 8
    },
    {
        "song_id": 6,
        "producer_id": 5
    },
    {
        "song_id": 7,
        "producer_id": 6
    },
    {
        "song_id": 8,
        "producer_id": 2
    },
    {
        "song_id": 8,
        "producer_id": 3
    },
    {
        "song_id": 9,
        "producer_id": 2
    },
    {
        "song_id": 9,
        "producer_id": 3
    },
    {
        "song_id": 10,
        "producer_id": 7
    }
]

for producer in producers:
    new_producer = Producer(
        id=producer['id'],
        name=producer['name'],
    )
    db.session.add(new_producer)

db.session.commit()


for writer in writers:
    new_writer = Writer(
        id=writer['id'],
        name=writer['name'],
    )
    db.session.add(new_writer)

db.session.commit()


for song in songs:
    new_song = Song(
        id=song['id'],
        title=song['title'],
        length=song['length'],
        album_id=song['album_id']
    )
    db.session.add(new_song)

db.session.commit()


for song_producer in song_producers:
    new_song_producer = SongProducer(
        song_id=song_producer['song_id'],
        producer_id=song_producer['producer_id'],
    )
    db.session.add(new_song_producer)

db.session.commit()

for song_writer in song_writers:
    new_song_writer = SongWriter(
        song_id=song_writer['song_id'],
        writer_id=song_writer['writer_id'],
    )
    db.session.add(new_song_writer)

db.session.commit()

for album in albums:
    new_album = Album(
        id=album['id'],
        title=album['title'],
        release_date=album['release_date'],
        total_length=album['total_length']
    )
    db.session.add(new_album)

db.session.commit()
