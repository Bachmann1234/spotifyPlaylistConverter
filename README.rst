Spotify To Google Music Playlist Translator
===========================================

This project is python 3

This project converts Spotify Playlists to 
Google Music Ones.

To extract a spotify playlist you need the following environment variables defined

SPOTIPY_CLIENT_ID=''
SPOTIPY_CLIENT_SECRET=''
SPOTIPY_REDIRECT_URI=''
SPOTIFY_USER=''

No typos there. the first 3 are SPOTIPY the api library im using. The last one is your spotify username

to extract a playlist simply run

extractpl <playlist_user> <playlist_id>

The script will walk you though an oauth flow then dump out some json. The oauth flow is skipped if the cached
token is valid

to upload a playlist file to google you need the following environment variables defined

export GUSER='' (google user name)


Then just run

uploadpl <playlist_json_file>

It will prompt for a password (sorry... no choice really) if you use 2-factor (good!) this needs to be an app specific
password
