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


def get_relevant_track_id(track, results):
    if not results:
        print("Could not find track: {} - {}".format(track.name, " ".join(track.artists)))
    else:
        print("✓")
        return results[0]['track']['nid']


def upload_playlist(gmusic_client, name, description, track_ids):
    gmusic_playlist = gmusic_client.create_playlist(name, description=description)
    gmusic_client.add_songs_to_playlist(gmusic_playlist, track_ids)


def get_query_results(gmusic_client, playlist):
    for track in playlist.tracks:
        query = "{} {}".format(track.name, " ".join(track.artists))
        yield (
            track,
            gmusic_client.search(
                query,
                max_results=5
            )['song_hits']
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

    track_ids = [get_relevant_track_id(track, results) for track, results in get_query_results(gmusic_client, playlist)]
    upload_playlist(gmusic_client, playlist.name, playlist.description, track_ids)


if __name__ == '__main__':
    sys.exit(main())
