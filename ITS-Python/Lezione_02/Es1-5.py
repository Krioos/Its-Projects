def conversion(temperature):
    temperature = "{:.1f}".format(5 *(temperature -32)/9)
    return temperature

temp = int(input("Inserire una temperatura in Fharenheit: "))
print(f"La temperatura data equivale a {conversion(temp)}° Celsius")
