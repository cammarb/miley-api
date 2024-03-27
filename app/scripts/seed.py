from datetime import datetime

from app.app import create_app
from app.extensions.database import db

from app.model.album import Album
from app.model.track import Track

app = create_app()
app.app_context().push()

albums = [
    {
        "title": "Meet Miley Cyrus",
        "slug": "meet-miley-cyrus",
        "release_date": datetime(2007, 6, 26),
        "total_length": "33:01",
        "tracks": [
            {
                "title": "See You Again",
                "slug": "see-you-again",
                "length": "3:10",
                "featuring_artist": None,
            },
            {
                "title": "East Northumberland High",
                "slug": "east-northumberland-high",
                "length": "3:24",
                "featuring_artist": None,
            },
            {
                "title": "Let's Dance",
                "slug": "lets-dance",
                "length": "3:03",
                "featuring_artist": None,
            },
            {
                "title": "G.N.O. (Girl's Night Out)",
                "slug": "gno-girls-night-out",
                "length": "3:38",
                "featuring_artist": None,
            },
            {
                "title": "Right Here",
                "slug": "right-here",
                "length": "2:45",
                "featuring_artist": None,
            },
            {
                "title": "As I Am",
                "slug": "as-i-am",
                "length": "3:46",
                "featuring_artist": None,
            },
            {
                "title": "Start All Over",
                "slug": "start-all-over",
                "length": "3:27",
                "featuring_artist": None,
            },
            {
                "title": "Clear",
                "slug": "clear",
                "length": "3:03",
                "featuring_artist": None,
            },
            {
                "title": "Good and Broken",
                "slug": "good-and-broken",
                "length": "2:56",
                "featuring_artist": None,
            },
            {
                "title": "I Miss You",
                "slug": "i-miss-you",
                "length": "3:58",
                "featuring_artist": None,
            },
        ],
    },
    {
        "title": "Breakout",
        "slug": "breakout",
        "release_date": datetime(2008, 7, 22),
        "total_length": "35:23",
        "tracks": [
            {
                "title": "Breakout",
                "slug": "breakout",
                "length": "3:26",
                "featuring_artist": None,
            },
            {
                "title": "7 Things",
                "slug": "7-things",
                "length": "3:33",
                "featuring_artist": None,
            },
            {
                "title": "The Driveway",
                "slug": "the-driveway",
                "length": "3:43",
                "featuring_artist": None,
            },
            {
                "title": "Girls Just Wanna Have Fun",
                "slug": "girls-just-wanna-have-fun",
                "length": "3:08",
                "featuring_artist": None,
            },
            {
                "title": "Full Circle",
                "slug": "full-circle",
                "length": "3:14",
                "featuring_artist": None,
            },
            {
                "title": "Fly on the Wall",
                "slug": "fly-on-the-wall",
                "length": "2:31",
                "featuring_artist": None,
            },
            {
                "title": "Bottom of the Ocean",
                "slug": "bottom-of-the-ocean",
                "length": "3:15",
                "featuring_artist": None,
            },
            {
                "title": "Wake Up America",
                "slug": "wake-up-america",
                "length": "2:46",
                "featuring_artist": None,
            },
            {
                "title": "These Four Walls",
                "slug": "these-four-walls",
                "length": "3:28",
                "featuring_artist": None,
            },
            {
                "title": "Simple Track",
                "slug": "simple-song",
                "length": "3:32",
                "featuring_artist": None,
            },
            {
                "title": "Goodbye",
                "slug": "goodbye",
                "length": "3:53",
                "featuring_artist": None,
            },
            {
                "title": "See You Again (Rock Mafia Remix)",
                "slug": "see-you-again-rock-mafia-remix",
                "length": "3:15",
                "featuring_artist": None,
            },
        ],
    },
    {
        "title": "Can't Be Tamed",
        "slug": "cant-be-tamed",
        "release_date": datetime(2010, 6, 18),
        "total_length": "41:22",
        "tracks": [
            {
                "title": "Liberty Walk",
                "slug": "liberty-walk",
                "length": "4:06",
                "featuring_artist": None,
            },
            {
                "title": "Who Owns My Heart",
                "slug": "who-owns-my-heart",
                "length": "3:34",
                "featuring_artist": None,
            },
            {
                "title": "Can't Be Tamed",
                "slug": "cant-be-tamed",
                "length": "2:48",
                "featuring_artist": None,
            },
            {
                "title": "Every Rose Has Its Thorn",
                "slug": "every-rose-has-its-thorn",
                "length": "3:48",
                "featuring_artist": None,
            },
            {
                "title": "Two More Lonely People",
                "slug": "two-more-lonely-people",
                "length": "3:09",
                "featuring_artist": None,
            },
            {
                "title": "Forgiveness and Love",
                "slug": "forgiveness-and-love",
                "length": "3:28",
                "featuring_artist": None,
            },
            {
                "title": "Permanent December",
                "slug": "permanent-december",
                "length": "3:38",
                "featuring_artist": None,
            },
            {
                "title": "Stay",
                "slug": "stay",
                "length": "4:22",
                "featuring_artist": None,
            },
            {
                "title": "Scars",
                "slug": "scars",
                "length": "3:42",
                "featuring_artist": None,
            },
            {
                "title": "Take Me Along",
                "slug": "take-me-along",
                "length": "4:09",
                "featuring_artist": None,
            },
            {
                "title": "Robot",
                "slug": "robot",
                "length": "3:43",
                "featuring_artist": None,
            },
            {
                "title": "My Heart Beats for Love",
                "slug": "my-heart-beats-for-love",
                "length": "3:42",
                "featuring_artist": None,
            },
        ],
    },
    {
        "title": "Bangerz",
        "slug": "bangerz",
        "release_date": datetime(2013, 10, 4),
        "total_length": "50:07",
        "tracks": [
            {
                "title": "Adore You",
                "slug": "adore-you",
                "length": "4:38",
                "featuring_artist": None,
            },
            {
                "title": "We Can't Stop",
                "slug": "we-cant-stop",
                "length": "3:51",
                "featuring_artist": None,
            },
            {
                "title": "SMS (Bangerz)",
                "slug": "sms-bangerz",
                "length": "2:49",
                "featuring_artist": "Britney Spears",
            },
            {
                "title": "4x4",
                "slug": "4x4",
                "length": "3:11",
                "featuring_artist": "Nelly",
            },
            {
                "title": "My Darlin'",
                "slug": "my-darlin",
                "length": "4:03",
                "featuring_artist": "Future",
            },
            {
                "title": "Wrecking Ball",
                "slug": "wrecking-ball",
                "length": "3:41",
                "featuring_artist": None,
            },
            {
                "title": "Love Money Party",
                "slug": "love-money-party",
                "length": "3:39",
                "featuring_artist": "Big Sean",
            },
            {
                "title": "#GETITRIGHT",
                "slug": "getitright",
                "length": "4:24",
                "featuring_artist": None,
            },
            {
                "title": "Drive",
                "slug": "drive",
                "length": "4:15",
                "featuring_artist": None,
            },
            {
                "title": "FU",
                "slug": "fu",
                "length": "3:51",
                "featuring_artist": "French Montana",
            },
            {
                "title": "Do My Thang",
                "slug": "do-my-thang",
                "length": "3:45",
                "featuring_artist": None,
            },
            {
                "title": "Maybe You're Right",
                "slug": "maybe-youre-right",
                "length": "3:33",
                "featuring_artist": None,
            },
            {
                "title": "Someone Else",
                "slug": "someone-else",
                "length": "4:48",
                "featuring_artist": None,
            },
        ],
    },
    {
        "title": "Younger Now",
        "slug": "younger-now",
        "release_date": datetime(2017, 9, 29),
        "total_length": "41:34",
        "tracks": [
            {
                "title": "Younger Now",
                "slug": "younger-now",
                "length": "4:08",
                "featuring_artist": None,
            },
            {
                "title": "Malibu",
                "slug": "malibu",
                "length": "3:51",
                "featuring_artist": None,
            },
            {
                "title": "Rainbowland",
                "slug": "rainbowland",
                "length": "4:25",
                "featuring_artist": "Dolly Parton",
            },
            {
                "title": "Week Without You",
                "slug": "week-without-you",
                "length": "3:43",
                "featuring_artist": None,
            },
            {
                "title": "Miss You so Much",
                "slug": "miss-you-so-much",
                "length": "4:53",
                "featuring_artist": None,
            },
            {
                "title": "I Would Die for You",
                "slug": "i-would-die-for-you",
                "length": "2:54",
                "featuring_artist": None,
            },
            {
                "title": "Thinkin'",
                "slug": "thinkin",
                "length": "4:05",
                "featuring_artist": None,
            },
            {
                "title": "Bad Mood",
                "slug": "bad-mood",
                "length": "2:59",
                "featuring_artist": None,
            },
            {
                "title": "Love Someone",
                "slug": "love-someone",
                "length": "3:17",
                "featuring_artist": None,
            },
            {
                "title": "She's Not Him",
                "slug": "shes-not-him",
                "length": "3:33",
                "featuring_artist": None,
            },
            {
                "title": "Inspired",
                "slug": "inspired",
                "length": "4:13",
                "featuring_artist": None,
            },
        ],
    },
    {
        "title": "Plastic Hearts",
        "slug": "plastic-hearts",
        "release_date": datetime(2020, 11, 27),
        "total_length": "50:30",
        "tracks": [
            {
                "title": "WTF Do I Know",
                "slug": "wtf-do-i-know",
                "length": "2:53",
                "featuring_artist": None,
            },
            {
                "title": "Plastic Hearts",
                "slug": "plastic-hearts",
                "length": "3:27",
                "featuring_artist": None,
            },
            {
                "title": "Angels like You",
                "slug": "angels-like-you",
                "length": "3:17",
                "featuring_artist": None,
            },
            {
                "title": "Prisoner",
                "slug": "prisoner",
                "length": "2:49",
                "featuring_artist": "Dua Lipa",
            },
            {
                "title": "Gimme What I Want",
                "slug": "gimme-what-i-want",
                "length": "3:09",
                "featuring_artist": None,
            },
            {
                "title": "Night Crawling",
                "slug": "night-crawling",
                "length": "4:00",
                "featuring_artist": "Billy Idol",
            },
            {
                "title": "Midnight Sky",
                "slug": "midnight-sky",
                "length": "3:43",
                "featuring_artist": None,
            },
            {
                "title": "High",
                "slug": "high",
                "length": "3:16",
                "featuring_artist": None,
            },
            {
                "title": "Hate Me",
                "slug": "hate-me",
                "length": "2:36",
                "featuring_artist": None,
            },
            {
                "title": "Bad Karma",
                "slug": "bad-karma",
                "length": "3:07",
                "featuring_artist": None,
            },
            {
                "title": "Never Be Me",
                "slug": "never-be-me",
                "length": "4:08",
                "featuring_artist": None,
            },
            {
                "title": "Golden G String",
                "slug": "golden-g-string",
                "length": "4:00",
                "featuring_artist": None,
            },
        ],
    },
]

for album_data in albums:
    album = Album(
        title=album_data["title"],
        slug=album_data["slug"],
        release_date=album_data["release_date"],
        total_length=album_data["total_length"],
    )
    db.session.add(album)

    for track_data in album_data["tracks"]:
        track = Track(
            title=track_data["title"],
            slug=track_data["slug"],
            length=track_data["length"],
            featuring_artist=track_data["featuring_artist"],
            album=album,
        )
        db.session.add(track)

db.session.commit()
