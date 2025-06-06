def caesar_cypher_encrypt(s:str, key:int)-> str:
    """
    Funzione che permette di cifrare tramite cesare una stringa. Ignora i caratteri speciali
    """
    out_string = ""
    key = key % 26
    for character in s.lower():
        if "a" <= character <= "z":
            shifted: int = (ord(character) - ord('a') + key) % 26 + ord('a')
            out_string += chr(shifted)
        else:
            out_string += character
    return out_string

def caesar_cypher_decript(s: str, key: int) -> str:
    out_string = ""
    key = key % 26
    for character in s:
        if "a" <= character <= "z":
            shifted = (ord(character) - ord('a') - key) % 26 + ord('a')
            out_string += chr(shifted)
        else:
            out_string += character
    return out_string


print(caesar_cypher_encrypt("casa", 28))
print(caesar_cypher_decript("ecuc", 28))
