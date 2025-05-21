class Song:
    count = 0
    artists = set ()
    genres = set ()
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre):
        self.name = name
        self.genre = genre
        self.artist = artist
        Song.add_to_artists(artist)
        Song.add_to_genres(genre)
        Song.add_song_to_count()
        Song.add_to_artist_count(artist)
        Song.add_to_genre_count(genre)

    @classmethod
    def add_to_artists(cls,artist):
        cls.artists.add(artist)

    @classmethod
    def add_to_genres(cls,genre):
        cls.genres.add(genre)


    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_artist_count(cls,artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    @classmethod
    def add_to_genre_count(cls,genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1