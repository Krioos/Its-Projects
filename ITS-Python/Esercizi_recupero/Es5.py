from random import randint
def multiply_below(threshold:int, lista: list[int])-> int:
    result = 1
    for elem in lista:
        if elem < threshold:
            result *= elem
    return result

def factorial(number:int)-> int:
    result: int = 1
    for i in range (2, number +1):
        result *= i
    return result

lista = [randint(1, 30) for _ in range(8)]
threshold = randint(1,30)
print(f"Il treshold è {threshold}")
print(f"La lista è {lista}")
print(multiply_below(threshold, lista))

print(factorial(0))


