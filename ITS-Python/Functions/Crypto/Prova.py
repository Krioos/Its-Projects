import base64

# La stringa in Base64 che vuoi decodificare
base64_string = "d2e5fgegd2bbfcbcc5cgc2eeeadcdae6c5dfc6bhcbefb5b5"

# Decodifica la stringa in Base64
decoded_bytes = base64.b64decode(base64_string)

# Converti i bytes decodificati in una stringa (assumendo che sia testo leggibile)
decoded_string = decoded_bytes.decode('utf-8', errors='ignore')

# Stampa il risultato
print(decoded_string)