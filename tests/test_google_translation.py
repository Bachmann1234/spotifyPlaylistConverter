from spotifyconverter.google import get_relevant_track_id
from spotifyconverter.models import Track


# These tests feel silly but im trying to follow the rule of "test all conditionals"
# and if I make this smarter this could be a nice starting point

DUMMY_TRACK = Track('wow', 'the wow album', ['nobody made this'], 'US-S1Z-99-00001')


def test_find_relevant_track_none():
    assert get_relevant_track_id(DUMMY_TRACK, []) is None


def test_find_relevant_track_results():
    # I dont really use track for this right now
    nid = 'Tq3nsmzeumhilpegkimjcnbr6aq'
    assert nid == get_relevant_track_id(DUMMY_TRACK, [{'track': {'nid': nid}}])
