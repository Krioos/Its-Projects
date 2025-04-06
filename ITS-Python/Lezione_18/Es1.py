import math

def safe_square_root(number: float) -> float:
    try:
        if number < 0:
            raise ValueError("Cannot compute the square root of a negative number.")
        return math.sqrt(number)
    except ValueError as e:
        return str(e)

print(safe_square_root(int(input("Insert a number: "))))