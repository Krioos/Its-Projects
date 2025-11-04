from random import choice
lista_nomi: list[str] = []
maximum: float  = float("-inf")
longest: list[str] = []
while len(lista_nomi) <= 30:
    nome: str = input("Inserisci un nome: ")
    if nome in lista_nomi  or len(nome) >= 20 or not nome:
        break
    else:
        lista_nomi.append(nome)
        if len(nome) >= maximum:
            maximum = len(nome)
            longest.append(nome)

print(f"Hai inserito {len(lista_nomi)} nomi distinti")
longest_name: str = choice(longest)
print(f"Il più lungo è {longest_name} con {len(longest_name)} caratteri")
