"""- 106-110 → 4.0
- 101-105 → 3.7
- 96-100 → 3.3
- 91-95 → 3.0
- 86-90 → 2.7
- 81-85 → 2.3
- 76-80 → 2.0
- 70-75 → 1.7
- 66-69 → 1.0
- Altro caso → "Voto non valid
"""

n:int = int(input("Inserire il voto di laurea: "))

match n:
    case n if n>= 106 and n<= 110:
        print("GPA 4.0")
    case n if n >= 101 and n <= 105:
        print("GPA 3.7")
    case n if n >=96 and n <=100:
        print("GPA 3.3")
    case n if n >= 91 and n <= 95:
        print("GPA 3.0")
    case n if n >= 86 and n <= 90:
        print("GPA 2.7")
    case n if n >= 81 and n <= 85:
        print("GPA 2.3")
    case n if n >= 76 and n <= 80:
        print("GPA 2.0")
    case n if n >= 70 and n <= 75:
        print("GPA 1.7")
    case n if n >= 66 and n <= 69:
        print("GPA 1.0")
    case _:
        print("Voto non valido")