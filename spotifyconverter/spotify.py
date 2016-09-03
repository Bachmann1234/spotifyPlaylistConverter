import argparse
import json
import os
import sys

import attr
import spotipy
import spotipy.util as util

from spotifyconverter.models import Track, Playlist


def extract_track_info(track):
    track_metadata = track['track']
    return Track(
        name=track_metadata['name'],
        album=track_metadata['album']['name'],
        artists=[artist['name'] for artist in track_metadata['artists']],
        isrc_code=track_metadata['external_ids'].get('isrc', 'unknown')
    )


def convert_spotify_playlist(spotify_playlist):
    return Playlist(
        name=spotify_playlist['name'],
        description=spotify_playlist['description'],
        tracks=[extract_track_info(track) for track in spotify_playlist['tracks']['items']]
    )


def get_playlist(username, playlist_user, playlist_id):
    token = util.prompt_for_user_token(username)
    sp = spotipy.Spotify(auth=token)
    return sp.user_playlist(
        playlist_user,
        playlist_id,
        fields="name,description,tracks.items(track(name,album(name),artists,external_ids))"
    )


def main():
    username = os.environ['SPOTIFY_USER']
    parser = argparse.ArgumentParser(
        description='Convert a playlist'
    )
    parser.add_argument(
        'playlist_user',
        type=str,
        help='User who owns the playlist'
    )
    parser.add_argument(
        'playlist_id',
        help='id for this playlist'
    )
    args = parser.parse_args()
    playlist = convert_spotify_playlist(
        get_playlist(
            username,
            args.playlist_user,
            args.playlist_id
        )
    )
    with open("{}.json".format(playlist.name), 'w') as output_file:
        output_file.write(
            json.dumps(
                attr.asdict(playlist),
                indent=4,
                sort_keys=True
            )
        )


if __name__ == '__main__':
    sys.exit(main())
