from random import randint

n_lanci: int = int(input("Inseire il numero di lanci: "))
sum_list: list[int] = [randint(1,6) + randint(1,6) for _ in range(n_lanci)]

possible_result = [i for i in range (2, 13)]
frequence = {}

for elem in possible_result:
    frequence[elem] = sum_list.count(elem)

most_frequent = ()
max = 0

for k,v in frequence.items():
    if v >= max:
        max = v
        most_frequent = (k,v)

print(f"Lista dei {n_lanci} lanci:\n{sum_list}")
print(f"Più frequente: {most_frequent[0]} uscito {(most_frequent[1] / n_lanci) * 100:.2F}% delle volte")