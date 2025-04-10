testa = 0
croce = 0

for i in range (8):
    lancio:str = input("Inserire il risultato del lancio (t o c): ").strip().lower()
    match lancio:
        case 't':
            testa += 1
        case 'c':
            croce += 1
        case _:
            print('Valore non valido')


if (testa + croce) > 0:
    print(f'Totale "testa": {testa}\nPercentuale "testa": {testa / (testa + croce) * 100:.2F}')
    print(f'Totale "croce": {croce}\nPercentuale "croce": {croce / (testa + croce) * 100:.2F}')
else:
    print("Errore nessun valore corretto inserito")