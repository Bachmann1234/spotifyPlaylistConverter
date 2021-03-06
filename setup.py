from setuptools import setup, find_packages

requirements = [
    'appdirs==1.4.0',
    'attrs==16.1.0',
    'beautifulsoup4==4.5.1',
    'cffi==1.7.0',
    'cryptography==1.5',
    'decorator==4.0.10',
    'future==0.15.2',
    'gmusicapi==10.0.1',
    'gpsoauth==0.4.0',
    'httplib2==0.9.2',
    'idna==2.1',
    'MechanicalSoup==0.4.0',
    'mock==2.0.0',
    'mutagen==1.34.1',
    'ndg-httpsclient==0.4.2',
    'oauth2client==3.0.0',
    'pbr==1.10.0',
    'proboscis==1.2.6.0',
    'protobuf==3.0.0b2',
    'py==1.4.31',
    'pyasn1==0.1.9',
    'pyasn1-modules==0.0.8',
    'pycparser==2.14',
    'pycryptodomex==3.4.2',
    'pyOpenSSL==16.1.0',
    'pytest==3.0.2',
    'python-dateutil==2.5.3',
    'requests==2.11.1',
    'rsa==3.4.2',
    'six==1.10.0',
    'spotipy==2.3.8',
    'validictory==1.0.2'
]

setup(
   name='spotifyPlaylistConverter',
   version='1.4',
   author='Matt Bachmann',
   url='https://github.com/Bachmann1234/playlistConverter',
   description='scripts to convert a Spotify playlist to a Google Music one',
   license='Apache 2.0',
   packages=find_packages(),
   install_requires=requirements,
   entry_points={
       'console_scripts': [
           'extractpl = spotifyconverter.spotify:main',
           'uploadpl = spotifyconverter.google:main'
       ]
   }
)
