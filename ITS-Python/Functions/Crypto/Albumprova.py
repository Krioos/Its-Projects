def make_album(artist, title, song_number = None):
    album = {}
    album[artist] = [title, song_number]
    return album

album1 = make_album("Bob Marley", "Nigga", 59)
print(album1)

album2 = make_album("Jay z", "Nigger", 3)
print(album2)

album3 = make_album("Aldo Moro", "Mi hanno rapito", 1)
print(album3)

