import attr

from spotifyconverter.models import Playlist


def test_to_dict():
    playlist = {
        "name": "Test Playlist",
        "description": "I am a playlist",
        "tracks": [
            {
                "isrc_code": "GBUM71107355",
                "album": "Ceremonials (Deluxe Edition)",
                "artists": [
                    "Florence + The Machine"
                ],
                "name": "Shake It Out"
            },
            {
                "isrc_code": "COF010010001",
                "album": "Al Son De Los Cueros - Hits de Salsa, Cumbia & Boogaloo",
                "artists": [
                    "Sonora Carruseles"
                ],
                "name": "La Salsa La Traigo Yo"
            }
        ]
    }

    assert playlist == attr.asdict(Playlist.from_dict(playlist))
