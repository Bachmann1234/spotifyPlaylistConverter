import attr


@attr.s(frozen=True)
class Playlist(object):
    name = attr.ib()
    description = attr.ib()
    tracks = attr.ib()

    @staticmethod
    def from_dict(dct):
        return Playlist(
            name=dct['name'],
            description=dct['description'],
            tracks=[Track.from_dict(track) for track in dct['tracks']]
        )


@attr.s(frozen=True)
class Track(object):
    name = attr.ib()
    album = attr.ib()
    artists = attr.ib()
    isrc_code = attr.ib()

    @staticmethod
    def from_dict(dct):
        return Track(
            name=dct['name'],
            album=dct['album'],
            artists=dct['artists'],
            isrc_code=dct['isrc_code']
        )
