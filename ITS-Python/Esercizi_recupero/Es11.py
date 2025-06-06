def count_unique_words(stringa:str)-> dict[str, int]:
    """
    Conta le parole uniche in una stringa e restituisce un dizionario con le parole come chiavi e il loro conteggio come valori.
    """
    tokens = stringa.split()
    conteggio = {}
    for token in tokens:
        token = token.lower().strip(",.!?;:")
        if token:
            if token in conteggio:
                conteggio[token] += 1
            else:
                conteggio[token] = 1
    return conteggio

# Esempio di utilizzo
text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text) # output == {'hello': 2, 'world': 2, 'python': 1}
print(output)