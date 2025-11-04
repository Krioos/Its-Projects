#1 leggo la riga di comando
import sys
import random

# print("Argomenti della riga di comando:", sys.argv)
if len(sys.argv) != 2:
    print("Usage: python randombit.py <nome file>")
    sys.exit(1)

#2 apro il file in lettura
content = None
with open(sys.argv[1], "rb") as f:
    #3 leggo il contenuto del file
    content = f.read()

pos = random.randint(0, len(content) - 1)
byte=content[pos]
#4 estraggo il bit casuale
bit = random.randint(0, 7)
valore = 1 << bit
byte = byte ^ valore
# aggiorno il byte nel file
content = content[:pos] + bytes([byte]) + content[pos + 1:]
#salvo il file
with open(sys.argv[1], "wb") as f:
    f.write(content)
print(f"Modificato il bit {bit} del byte alla posizione {pos} nel file {sys.argv[1]}")
sys.exit(0)