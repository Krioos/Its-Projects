from Catalog import MovieCatalog

def test_remove_existing_movie():
    catalog = MovieCatalog()
    catalog.add_movie("Nolan", ["Inception", "Interstellar"])
    result = catalog.remove_movie("Nolan", "Inception")
    assert "rimosso" in result
    assert catalog.get_catalog() == {"Nolan": ["Interstellar"]}

def test_remove_last_movie_and_keep_director():
    catalog = MovieCatalog()
    catalog.add_movie("Nolan", ["Inception"])
    result = catalog.remove_movie("Nolan", "Inception")
    assert result == "Nolan non ha più film"
    assert "Nolan" in catalog.get_catalog()

def test_remove_last_movie_and_delete_director():
    catalog = MovieCatalog()
    catalog.add_movie("Nolan", ["Inception"])
    result = catalog.remove_movie("Nolan", "Inception", auto_confirm_remove=True)
    assert result == "Nolan rimosso dal catalogo"
    assert "Nolan" not in catalog.get_catalog()

def test_remove_movie_director_not_found():
    catalog = MovieCatalog()
    result = catalog.remove_movie("Spielberg", "Jaws")
    assert result == "Errore: regista non trovato"

def test_remove_movie_not_found():
    catalog = MovieCatalog()
    catalog.add_movie("Nolan", ["Inception"])
    result = catalog.remove_movie("Nolan", "Tenet")
    assert result == "Errore: film non trovato"

def test_list_directors():
    catalog = MovieCatalog()
    catalog.add_movie("Nolan", ["Inception", "Tenet"])
    catalog.add_movie("Spielberg", ["Jaws"])
    directors = catalog.list_directors()
    assert "Nolan" in directors
    assert "Spielberg" in directors
    assert len(directors) == 2

def test_get_movies_by_director_found():
    catalog = MovieCatalog()
    catalog.add_movie("Nolan", ["Inception", "Tenet"])
    movies = catalog.get_movies_by_director("Nolan")
    assert "Inception" in movies
    assert "Tenet" in movies
    assert len(movies) == 2

def test_get_movies_by_director_not_found():
    catalog = MovieCatalog()
    catalog.add_movie("Nolan", ["Inception"])
    result = catalog.get_movies_by_director("Tarantino")
    assert result == "Errore: Tarantino non trovato"

def test_search_movies_by_title_found():
    catalog = MovieCatalog()
    catalog.add_movie("Nolan", ["Inception", "Interstellar", "Tenet"])
    catalog.add_movie("Spielberg", ["Indiana Jones", "Jaws"])
    result = catalog.search_movies_by_title("in")
    assert "Nolan" in result
    assert "Spielberg" in result
    assert "Inception" in result["Nolan"]
    assert "Indiana Jones" in result["Spielberg"]

def test_search_movies_by_title_not_found():
    catalog = MovieCatalog()
    catalog.add_movie("Nolan", ["Tenet"])
    result = catalog.search_movies_by_title("Matrix")
    assert result == "Nessun film trovato"

# Esegui tutti i test
if __name__ == "__main__":
    test_remove_existing_movie()
    test_remove_last_movie_and_keep_director()
    test_remove_last_movie_and_delete_director()
    test_remove_movie_director_not_found()
    test_remove_movie_not_found()
    test_list_directors()
    test_get_movies_by_director_found()
    test_get_movies_by_director_not_found()
    test_search_movies_by_title_found()
    test_search_movies_by_title_not_found()
    print("✅ Tutti i test superati con successo.")
