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

I find your tests lacking
=========================

Yeah, I hear ya. So I tried a philosophy for testing this where I made the code as declarative possible. Any conditionals
get a test. Right now I *think* its basically a situation where it either works or it does not. There are not many "cases"

As I use it I may find cases (error handling comes to mind) and I will add tests as I go.

Basically, ive gone down the route of stubbing the api or recording a set of api responses and ive found that more often
then not the api changes and my tests pass but the code breaks.

A set of integration tests is an option, and if these two scripts start branching (right now there is basically the one path)
that will be something I consider.

And if this gets popular I will probably add a nightly job to test the one path so I can catch api problems faster.

Disagree with the plan? Lets chat, i'll learn something

