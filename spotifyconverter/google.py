import argparse
import json
import os
import sys
from getpass import getpass

from gmusicapi.protocol.shared import Call

from spotifyconverter.models import Playlist
from gmusicapi import Mobileclient

# Work around broken unicode handling
Call.gets_logged = False


def upload_playlist(gmusic_client, playlist, track_ids):
    gmusic_playlist = gmusic_client.create_playlist(playlist.name, description=playlist.description)
    gmusic_client.add_songs_to_playlist(gmusic_playlist, track_ids)


def find_relevant_track(search_results, track):
    # This could potentially get smarter....
    if not search_results:
        print("Could not find track: {} - {}".format(track.name, " ".join(track.artists)))
        return None
    else:
        print("✓")
        return search_results[0]['track']['nid']


def get_track_id(gmusic_client, track):
    query = "{} {}".format(track.name, " ".join(track.artists))
    search_results = gmusic_client.search(
        query,
        max_results=5
    )['song_hits']
    return find_relevant_track(search_results, track)


def get_track_ids(gmusic_client, playlist):
    return list(
        filter(
            None,
            [get_track_id(gmusic_client, track) for track in playlist.tracks]
        )
    )


def main():
    parser = argparse.ArgumentParser(
        description='Convert a playlist'
    )
    parser.add_argument(
        'playlist_file',
        type=str,
        help='json file with the playlist info'
    )

    username = os.environ["GUSER"]
    password = getpass(
        "Google Password (if 2-factor app specific password) (sorry... no official gmusic api so no oauth):"
    )
    gmusic_client = Mobileclient()
    gmusic_client.login(username, password, Mobileclient.FROM_MAC_ADDRESS)

    args = parser.parse_args()
    with open(args.playlist_file) as infile:
        playlist = Playlist.from_dict(
            json.loads(infile.read())
        )

    track_ids = get_track_ids(gmusic_client, playlist)
    upload_playlist(gmusic_client, playlist, track_ids)


if __name__ == '__main__':
    sys.exit(main())
