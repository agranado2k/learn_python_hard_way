class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday_lyric = ["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"]
happy_bday = Song(happy_bday_lyric)

bulls_on_parade_lyric = ["They rally around the family",
                        "With pockets full of shells"]
bulls_on_parade = Song(bulls_on_parade_lyric)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
