from spotifyconverter.google import find_relevant_track
from spotifyconverter.models import Track

example_search = """
[{
    'track': {
        'album': 'Work Out',
        'albumArtRef': [{
            'aspectRatio': '1',
            'autogen': False,
            'kind': 'sj#imageRef',
            'url': 'http://lh5.ggpht.com/DVIg4GiD6msHfgPs_Vu_2eRxCyAoz0fFdxj5w...'
        }],
        'albumArtist': 'J.Cole',
        'albumAvailableForPurchase': True,
        'albumId': 'Bfp2tuhynyqppnp6zennhmf6w3y',
        'artist': 'J Cole',
        'artistId': ['Ajgnxme45wcqqv44vykrleifpji', 'Ampniqsqcwxk7btbgh5ycujij5i'],
        'composer': '',
        'discNumber': 1,
        'durationMillis': '234000',
        'estimatedSize': '9368582',
        'explicitType': '1',
        'genre': 'Pop',
        'kind': 'sj#track',
        'nid': 'Tq3nsmzeumhilpegkimjcnbr6aq',
        'primaryVideo': {
            'id': '6PN78PS_QsM',
            'kind': 'sj#video',
            'thumbnails': [{
                'height': 180,
                'url': 'https://i.ytimg.com/vi/6PN78PS_QsM/mqdefault.jpg',
                'width': 320
            }]
        },
        'storeId': 'Tq3nsmzeumhilpegkimjcnbr6aq',
        'title': 'Work Out',
        'trackAvailableForPurchase': True,
        'trackAvailableForSubscription': True,
        'trackNumber': 1,
        'trackType': '7',
        'year': 2011
    },
    'type': '1'
}]
"""


# These tests feel silly but im trying to follow the rule of "test all conditionals"
# and if I make this smarter this could be a nice starting point

def test_find_relevant_track_none():
    assert find_relevant_track([], Track()) is None


def test_find_relevant_track_results():
    # I dont really use track for this right now
    assert 'Tq3nsmzeumhilpegkimjcnbr6aq' == find_relevant_track(example_search, Track())
