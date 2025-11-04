def favorite_book(title):
    print("%s is one of my favorite books" %title)

book = input("Insert the title of a book (N to end): ")
while book != "N":

    favorite_book(book)
    book = input("Insert the title of a book (N to end): ")
