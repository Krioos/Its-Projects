def make_album(artist, title, song_number = None):
    album = {}
    album[artist] = [title, song_number]
    return album

album1 = make_album("Bob Marley", "Album 1", 59)
print(album1)

album2 = make_album("Jay z", "Album 2", 3)
print(album2)

album3 = make_album("Pippo", "Album 3", 1)
print(album3)

