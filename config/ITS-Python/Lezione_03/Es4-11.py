pizzas:list[str] = ["Boscaiola", "Margherita", "Crostino"] 

friends_pizzas:list[str] = pizzas.copy()

pizzas.append("Halloween")
friends_pizzas.append("Tirolese")
print(f"{pizzas}\n{friends_pizzas}")

for elem in pizzas:
    print(f"I really like {elem} pizza")

for elem in friends_pizzas:
    print(f"My freind really loves {elem} pizzas")
    
pizzas.pop()
friends_pizzas.pop(0)

print(f"{pizzas}\n{friends_pizzas}")