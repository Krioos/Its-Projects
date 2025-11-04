
max:float = float("-inf")
min: float = float("inf")
for i in range(1,1000001):
    if i >= max:
        max = i
    if i <= min:
        min = i

print(f"Il massimo è {max} il minimo è {min}")
print(f"La somma dei pirmi 10^6 numeri è {sum(range(1,1000001))}")