def make_album(artist, title, song_number = None):
    album = {}
    album[artist] = [title, song_number]
    return album
flag = "Y"
while True:
    artist = input("Insert an artist: ")
    album = input("Insert an album: ")
    song_number = input("Insert the number of songs in the album: ")
    album = make_album(artist, album, song_number)
    flag = input()