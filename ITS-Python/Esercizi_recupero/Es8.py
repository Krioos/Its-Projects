class Movie():
    def __init__(self, movie_id: str, title: str, director:str)-> None:
        self._movie_id: str = movie_id
        self._title: str = title
        self._director: str = director
        self._is_rented: bool = False

    def rent(self)-> None | str:
        if not self._is_rented:
            self._is_rented = True
        else:
            return f"Il film {self._title} è già stato noleggiato"
    
    def return_movie(self)-> None | str:
        if self._is_rented:
            self._is_rented = False
        else:
            return f"Il film {self._title} non è stato noleggiato da questo cliente"
        
class Customer():
    def __init__(self, customer_id: str, name:str)-> None:
        self._customer_id: str = customer_id
        self._name: str = name
        self._rented_movies: list[Movie] = []
    
    def rent_movie(self, movie: Movie)-> None | str:
        if movie.rent() is None: # Il metodo rent restituisce None se e solo se il film è stato noleggiato correttamente
            self._rented_movies.append(movie)
        else:
            return movie.rent()

    def return_movie(self, movie: Movie)-> None | str:
        if movie.return_movie() is None: # Il metodo return_movie restituisce None se e solo se il film è stato restituito correttamente
            self._rented_movies.remove(movie)
        else:
            return movie.return_movie()

class VideoRentalStore():
    def __init__(self)->None:
        self._movies: dict[str, Movie] = {}
        self._customers: dict[str, Customer] = {}

    def add_movie(self, movie_id: str, title: str, director: str)-> None:
        if movie_id not in self._movies:
            self._movies[movie_id] = Movie(movie_id, title, director)
        else:
            return f"Il film con ID {movie_id} esiste già"
    
    def register_customer(self, customer_id: str, name: str)-> None:
        if customer_id not in self._customers:
            self._customers[customer_id] = Customer(customer_id, name)
        else:
            return f"Il cliente con ID {customer_id} esiste già"
    
    def rent_movie(self, customer_id: str, movie_id: str)-> None | str:
        if customer_id in self._customers and movie_id in self._movies:
            customer: Customer = self._customers[customer_id]
            movie: Movie = self._movies[movie_id]
            customer.rent_movie(movie)
        else:
            return "Cliente o film non trovato"
        
    def return_movie(self, customer_id: str, movie_id: str)-> None | str:
        if customer_id in self._customers and movie_id in self._movies:
            customer: Customer = self._customers[customer_id]
            movie: Movie = self._movies[movie_id]
            customer.return_movie(movie)
        else:
            return "Cliente o film non trovato"
    
    def get_rented_movies(self, customer_id: str)-> list[Movie] | list:
        if customer_id in self._customers:
            customer: Customer = self._customers[customer_id]
            return customer._rented_movies
        else:
            print("Cliente non trovato")
            return []



store = VideoRentalStore()
store.add_movie("001", "Inception", "Nolan")
store.add_movie("002", "Matrix", "Wachowski")

store.register_customer("c01", "Alice")

print(store.rent_movie("c01", "001"))  # None (successo)
print(store.rent_movie("c01", "001"))  # Film già noleggiato
print(store.rent_movie("c01", "002"))  # None (successo)

print(store.get_rented_movies("c01"))  # ['Inception', 'Matrix']

print(store.return_movie("c01", "001"))  # None (successo)
print(store.return_movie("c01", "001"))  # Film non è stato noleggiato

print(store.get_rented_movies("c01"))  # ['Matrix']
