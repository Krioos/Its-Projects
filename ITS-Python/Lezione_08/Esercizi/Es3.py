class Book():
    def __init__(self, title:str, author:str, isbn:str)-> None:
        self.title = title
        self.author = author
        self.isbn = int(isbn)

    def __str__(self)-> str:
        return f"{self.author}\n{self.title}\n{self.isbn}"
    
    @classmethod
    def from_string(cls, stringa)-> object:
        lista = stringa.split(",")
        return cls(lista[0].strip(), lista[1].strip(), lista[2].strip())

class Member():
    def __init__(self, name: str, member_id: int)-> None:
        self.name = name
        self.member_id  = member_id
        self.borrowed_books = list()

    def borrow_book(self, book: Book)-> None:
        self.borrowed_books.append(book)
    
    def return_book(self, book: Book)-> None:
        try:
            self.borrowed_books.remove(book)
        except Exception:
            raise Exception(f"Libro '{book.title}' non trovato in lista di libri presi in prestito")
        except Exception:
            raise Exception(f"Error the book {book.title} not in member books list")
            
    def __str__(self)-> str:
        books_titles = [book.title for book in self.borrowed_books]
        return f"Name: {self.name}\nId: {self.member_id}\nBooks: {books_titles}"
    
    @classmethod
    def from_string(cls, stringa: str):
        lista = stringa.split(",")
        return cls(lista[0].strip(), lista[1].strip())
    
class Library():
    total_books = 0
    def __init__(self)-> None:
        self.books = list()
        self.members = list()

    def register_member(self, member: Member)-> None:
        self.members.append(member)

    def add_book(self, book: Book)-> None:
        self.books.append(book)
        Library.total_books += 1
    
    def remove_book(self, book: Book)-> None:
        try:
            self.books.remove(book)
            Library.total_books -= 1
        except Exception:
            raise Exception(f"Error book {book.title} not in library")
    
    def return_book(self, member: Member, book: Book)-> None:
        try:    
            member.return_book(book)
            self.add_book(book)
        except Exception as e:
            print(e)
        

    def lend_book(self, member, book)-> None:
        if member in self.members:
            try:
                self.remove_book(book)
                member.borrow_book(book)
            except Exception:
                raise Exception(f"No book called {book.title} in library")
    def return_book(self, member, book)-> None:
        try:
            member.return_book(book)
            self.add_book(book)
        except Exception:
            raise Exception("Operazione non eseguita")

    def lend_book(self, member: Member, book: Book)-> None:
        try:
            self.remove_book(book)
            member.borrow_book(book)
        except Exception as e:
            print(e)

    def __str__(self)-> str:
        book_titles = [book.title for book in self.books]
        members_names = [member.name for member in self.members]
        return f"The librabry has {self.total_books} books which are {book_titles}\nLibrabry members: {members_names}"
    
    @classmethod
    def library_statistics(self)-> None:
        print(f"The total numbers of books are {Library.total_books}")
    

# Driver Program
if __name__ == "__main__":
    # Create a library instance
    my_library = Library()

    # Create instances of Book using from_string
    book1 = Book.from_string("The Hitchhiker's Guide to the Galaxy, Douglas Adams, 9780345391803")
    book2 = Book.from_string("1984, George Orwell, 9780451524935")
    book3 = Book.from_string("To Kill a Mockingbird, Harper Lee, 9780061120084")

    # Create instances of Member using from_string
    member1 = Member.from_string("Alice Smith, 1001")
    member2 = Member.from_string("Bob Johnson, 1002")

    print("--- Initial Library State ---")
    print(my_library)
    Library.library_statistics()
    print("-" * 30)

    # Add books to the library
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    print("\n--- Library State After Adding Books ---")
    print(my_library)
    Library.library_statistics()
    print("-" * 30)

    # Register members to the library
    my_library.register_member(member1)
    my_library.register_member(member2)

    print("\n--- Library State After Registering Members ---")
    print(my_library)
    Library.library_statistics()
    print("-" * 30)

    print("\n--- Library State Before Lending Books ---")
    print(my_library)
    print("Member 1:", member1)
    print("Member 2:", member2)
    Library.library_statistics()
    print("-" * 30)

    # Lend books to members
    my_library.lend_book(member1, book1)
    my_library.lend_book(member2, book2)
    my_library.lend_book(member1, book3) # Alice borrows another book

    print("\n--- Library State After Lending Books ---")
    print(my_library)
    print("Member 1:", member1)
    print("Member 2:", member2)
    Library.library_statistics()
    print("-" * 30)

    # Simulate a return
    my_library.return_book(member1, book1)

    print("\n--- Library State After a Book is Returned ---")
    print(my_library)
    print("Member 1:", member1)
    print("Member 2:", member2)
    Library.library_statistics()
    print("-" * 30)

    # Attempt to lend a book that's not in the library
    book_not_in_library = Book("Non-existent Book", "Someone", "1234567890")
    my_library.lend_book(member2, book_not_in_library)
    print("\n--- Library State After Attempting to Lend Non-existent Book ---")
    print(my_library)
    print("Member 2:", member2)
    Library.library_statistics()
    print("-" * 30)

    # Attempt to return a book not borrowed by the member
    my_library.return_book(member2, book1)
    print("\n--- Library State After Attempting to Return Not Borrowed Book ---")
    print(my_library)
    print("Member 2:", member2)
    Library.library_statistics()
    print("-" * 30)