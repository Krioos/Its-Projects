class MovieCatalog:
    def __init__(self)-> None:
        self.set_catalog()

    def set_catalog(self)-> None:
        self.catalog = {}
    
    def get_catalog(self)-> dict[str: list[str]]:
        return self.catalog

    def __str__(self)-> str:
        result = ""
        for k, v in self.catalog.items():
            result += f"Director {k}:\n"
            for movie in v:
                result += f"\t{movie}\n"
            result += "\n"
        return result.strip()

    def add_movie(self, director_name: str, movies: list)-> None:
        if director_name not in self.catalog:
            self.catalog[director_name] = []
        self.catalog[director_name].extend(movies)
        self.catalog[director_name] = list(set(self.catalog[director_name]))

    def remove_movie(self, director_name, movie_name, auto_confirm_remove=False)-> str:
        if director_name not in self.catalog:
            return("Errore: regista non trovato")
        if movie_name not in self.catalog[director_name]:
            return("Errore: film non trovato")
        else:
            self.catalog[director_name].remove(movie_name)
        if len(self.catalog[director_name]) == 0:
            if auto_confirm_remove:
                self.catalog.pop(director_name)
                return f"{director_name} rimosso dal catalogo"
            else:
                return f"{director_name} non ha più film"

        return f"{movie_name} rimosso da {director_name}"

    def list_directors(self)-> list[str] | str:
        return list(self.catalog.keys()) if self.catalog else "Errore: il catalogo è vuoto"
    
    def get_movies_by_director(self, director_name)-> list[str] | str:
        if director_name not in self.catalog:
            return f"Errore: {director_name} non trovato"
        else:
            return self.catalog[director_name]
        
    def search_movies_by_title(self, title)-> dict[str: list[str]] | str:
        result = {}
        for director, movies in self.catalog.items():
            matches = []
            for movie in movies:
                if title.lower() in movie.lower():
                    matches.append(movie)
                if matches:
                    result[director] = matches
        return result if result else f"Nessun film trovato"
        