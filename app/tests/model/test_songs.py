from api.extensions.database import db,
from api.model.songs import Song


def test_song_update(client):
    # updates song's properties
    song = Song(
        title='I Miss',
        album_id=1,
        length="3:58"
    )
    db.session.add(song)
    db.session.commit()

    song.title = "I Miss You"
    song.save()

    updated_song = Song.query.filter_by(id=10).first()
    assert updated_song.title == "I Miss You"
