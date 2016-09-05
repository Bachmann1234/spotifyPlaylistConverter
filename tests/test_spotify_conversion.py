import json
import os

from spotifyconverter.models import Playlist, Track
from spotifyconverter.spotify import convert_spotify_playlist, extract_track_info

with open(os.path.join(os.path.dirname(__file__), 'example_spotify_playlist.json')) as infile:
    TEST_PLAYLIST = json.loads(infile.read())


def test_extract_track_info():
    expected = Track(
        name='Test Track',
        album='Test Album',
        artists=['The Test Artist'],
        isrc_code='dasudasd'
    )
    result = extract_track_info(TEST_PLAYLIST['tracks']['items'][0])
    assert expected == result


def test_convert_playlist():
    result_playlist = convert_spotify_playlist(TEST_PLAYLIST)
    expected_playlist = Playlist(
        name='Test Playlist',
        description='Test Playlist description',
        tracks=[
            Track(
                name='Test Track',
                album='Test Album',
                artists=['The Test Artist'],
                isrc_code='dasudasd'
            ),
            Track(
                name='OMG TEST',
                album='Test Album Two',
                artists=['The Other Test'],
                isrc_code='3213a123123'
            )
        ]
    )
    assert expected_playlist == result_playlist
