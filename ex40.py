class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            
# Define the lyrics in separate variables
happy_bday_lyrics = [
    "Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there!"
]

bulls_on_parade_lyrics = [
    "They rally around tha family",
    "With pockets full of shells"
]

# Pass the lyrics variables to the Song class
happyBday = Song(happy_bday_lyrics)
bullsOnParade = Song(bulls_on_parade_lyrics)
# Call the method to sing the songs
happyBday.sing_me_a_song()
bullsOnParade.sing_me_a_song()