from math import factorial
from scipy import stats
def binomial(n: int, k:int, p:float)-> float:
    if k  not in range(0,n):
        raise ValueError("Errore il valore di k non è corretto")
    binomiale = factorial(n)/(factorial(k) * factorial(n - k))
    return binomiale * (p ** k) * (1 - p) ** (n - k)


k = 3
n = 5
p = 0.5

print(binomial(n,k,p))
print(stats.binom.pmf(k, n, p))