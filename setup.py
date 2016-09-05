from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
   name='spotifyPlaylistConverter',
   version='1.1',
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
