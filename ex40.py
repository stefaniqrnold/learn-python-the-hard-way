class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            
happyBday = Song(["""Happy birthday to you\nI don't want to get sued\nSo I'll stop right there!"""])

bullsOnParade = Song(["""They rally around tha family\nWith pockets full of shells"""])

happyBday.sing_me_a_song()

bullsOnParade.sing_me_a_song()