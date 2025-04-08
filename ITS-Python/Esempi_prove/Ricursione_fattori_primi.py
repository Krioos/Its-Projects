def prime_factors(n: int, divisore: int = 2) -> list[int]:
    if n == 1:
        return []
    if n % divisore == 0:
        return [divisore] + prime_factors(n // divisore, divisore)
    else:
        return prime_factors(n, divisore + 1)
    

print(prime_factors(int(input("Inserire il numero di cui si vogliono calcolare i fattori primi: "))))