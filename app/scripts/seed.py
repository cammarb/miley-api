from app.app import create_app
from app.songs.models import Song
from app.albums.models import Album
from app.extensions.database import db

app = create_app()
app.app_context().push()

discography = {
    "songs": "/api/songs",
    "albums": "/api/albums"
}

# Albums
total_songs = 0
tracklist = []

albums = [
    {
        "id": 1,
        "title": "Meet Miley Cyrus",
        "release_date": "2007-06-27",
        "tracklist": tracklist,
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
        "total_songs": total_songs,
        "total_lenght": "33:05"
    }
]

# Songs
songs = [
    {
        {
            "id": "1",
            "title": "See You Again",
            "length": "3:10",
            "album_id": 1,
            "writers": [
                "Destiny Hope Cyrus",
                "Armato",
                "James"
            ],
            "producers": [
                "Armato",
                "James"
            ]
        },
        {
            "id": "2",
            "title": "East Northumberland High",
            "length": "3:24",
            "album_id": 1,
            "writers": [
                "Armato",
                "James",
                "Samantha Jo Moore"
            ],
            "producers": [
                "Armato",
                "James"
            ]
        },
        {
            "id": "3",
            "title": "Let's Dance",
            "length": "3:03",
            "album_id": 1,
            "writers": [
                "Destiny Hope Cyrus",
                "Armato",
                "James"
            ],
            "producers": [
                "Armato",
                "James"
            ]
        },
        {
            "id": "4",
            "title": "G.N.O. (Girl's Night Out)",
            "length": "3:38",
            "album_id": 1,
            "writers": [
                "Destiny Hope Cyrus",
                "Matthew Wilder",
                "Tamara Dunn"
            ],
            "producers": [
                "Wilder"
            ]
        },
        {
            "id": "5",
            "title": "Right Here",
            "length": "2:45",
            "album_id": 1,
            "writers": [
                "Destiny Hope Cyrus",
                "Armato",
                "James"
            ],
            "producers": [
                "Armato",
                "James"
            ]
        },
        {
            "id": "6",
            "title": "As I Am",
            "length": "3:46",
            "album_id": 1,
            "writers": [
                "Destiny Hope Cyrus",
                "Shelley Peiken",
                "Xandy Barry"
            ],
            "producers": [
                "Xandy Barry",
                "Wally Gagel"
            ]
        },
        {
            "id": "7",
            "title": "Start All Over",
            "length": "3:27",
            "album_id": 1,
            "writers": [
                "Scott Cutler",
                "Anne Preven",
                "Fefe Dobson"
            ],
            "producers": [
                "Annetenna"
            ]
        },
        {
            "id": "8",
            "title": "Clear",
            "length": "3:03",
            "album_id": 1,
            "writers": [
                "Destiny Hope Cyrus",
                "Peiken",
                "Xandy Barry"
            ],
            "producers": [
                "Armato",
                "James"
            ]
        },
        {
            "id": "9",
            "title": "Good and Broken",
            "length": "2:56",
            "album_id": 1,
            "writers": [
                "Destiny Hope Cyrus",
                "Armato",
                "James"
            ],
            "producers": [
                "Armato",
                "James"
            ]
        },
        {
            "id": "10",
            "title": "I Miss You",
            "length": "3:58",
            "album_id": 1,
            "writers": [
                "Destiny Hope Cyrus",
                "Brian Green",
                "Wendi Foy Green"
            ],
            "producers": [
                "B. Green"
            ]
        }
    }
]

for id, album in albums.items():
    for song in songs.items():
        if song['id'] == id:
            total_songs = total_songs + 1
            tracklist.append(song['title'])

    new_album = Album(
        id=album['id'],
        title=album['title'],
        release_date=album['release_date'],
        tracklist=album['tracklist'],
        total_lenght=album['total_lenght'])
    db.session.add(new_album)

db.session.commit()


for id, song in songs.items():
    new_song = Song(
        id=id,
        title=song['title'],
        length=song['length'],
        album_id=song['album_id'],
        writers=song['writers'],
        producers=song['producers'])
    db.session.add(new_song)

db.session.commit()
