def count_primes(number: int) -> int:
    count: int = 0
    for i in range(2, number + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            count += 1
    return count


print(count_primes(100))
        




def print_big(letter:str)-> None:
    a = "  *  \n"+" **  \n"+"*****\n"+"*    *\n"+"*    *\n"
    dict = {"a": a}
    if letter.lower() in dict.keys():
        print(dict[letter])

print_big("a")