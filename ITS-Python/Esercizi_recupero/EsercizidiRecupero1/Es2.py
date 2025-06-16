sequence = []
while True:
    x = input("Inserire un numero intero positivo: ")
    try:
        x = int(x)
    except:
        print("Il valore non è un intero, inserirne uno per favore")
        continue
    while True:
        number: int = input("Inserire un valore (0 per terminare): ")
        try:
            int(number)
        except:
            print("Il valore non è un intero, inserirne uno per favore")
            continue
        else:
            number = int(number)
            if number == 0:
                break
            elif number < 0:
                continue
            else:
                sequence.append(number)
    break


occ = sequence.count(x)

if x in sequence:
    pos = sequence.index(x)
else:
    print(f"Il valore {x} non è nella sequenza")

sum_others = sum(num for num in sequence if num != x)

print(sequence)
print(f"{x} contanto {occ} volte")
print(f"Valore {x} trovato in posizione {pos}")
print(f"Somma dei valori diversi da {x}: {sum_others}")