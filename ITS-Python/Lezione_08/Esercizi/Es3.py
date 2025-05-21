class Book():
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.author}\n{self.title}\n{self.isbn}"
    
    @classmethod
    def from_string(cls, stringa)-> object:
        lista = stringa.split(",")
        return cls(lista[0].strip(), lista[1].strip(), lista[2].strip())

class Member():
    def __init__(self, name, member_id):
        self.name = name
        self.member_id  = member_id
        self.borrowed_books = list()

    def borrow_book(self, book):
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        try:
            self.borrowed_books.remove(book)
        except ValueError:
            print("Libro non trovato in lista di libri presi in prestito")
            
    def __str__(self):
        return f"Nome: {self.name}\nId: {self.member_id}\nLibri: {self.borrowed_books}"
    
    @classmethod
    def from_string(cls, stringa):
        lista = stringa.split(",")
        return cls(lista[0].strip(), lista[1].strip())
    
book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
divina_commedia: Book = Book.from_string(book_str)

print(divina_commedia)


member_str: str = "Luca, 376229"
member_one: Member = Member.from_string(member_str)
print(member_one)
member_one.borrow_book(divina_commedia.title)
print(member_one)
member_one.return_book(divina_commedia.title)
print(member_one)