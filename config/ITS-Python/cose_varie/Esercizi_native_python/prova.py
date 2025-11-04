sum1 = 0
sum2 = 0
sum3 = 0
for i in range (1,11):
    sum1 += i
for i in range(20,38):
    sum2 += i
for i in range(35,50):
    sum3 += i
    
print(f"{sum1}\n{sum2}\n{sum3}")

ranges =[(1,11),(20,38),(35,50)]
for elem in ranges:
    sum = 0
    for i in range(elem[0],elem[1]):
        sum += i
    print(f"La somma dei numeri interi con estremi {elem} è {sum}")

def integer_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum

ranges = (int(input("Inserire lo start: ")), int(input("Inserire l'end: ")))
print(f"La somma dei numeri interi da {ranges[0]} a {ranges[1]}: {integer_sum(ranges[0], ranges[1])}")
        