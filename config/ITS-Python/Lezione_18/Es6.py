import math

class FractionError(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidDenominatorError(FractionError):
    """Raised when the denominator is zero."""
    def __init__(self, message="Denominator cannot be zero."):
        self.message = message
        super().__init__(self.message)

class InvalidFractionError(FractionError):
    """Raised when a fraction is invalid."""
    def __init__(self, message="Invalid fraction operation."):
        self.message = message
        super().__init__(self.message)

class Fraction():
    def __init__(self, numerator, denominator):
        try:
            if denominator == 0:
                raise InvalidDenominatorError("Can not create functions with denominator 0")
            self.numerator = numerator
            self.denominator = denominator
            self.simplify()
        except InvalidDenominatorError as e:
            print(f"Error {e}")
    def simplify(self):
        try:
            gcd = math.gcd(self.numerator, self.denominator)
            self.numerator //= gcd
            self.denominator //= gcd
            if self.denominator < 0:
                self.numerator = -self.numerator
                self.denominator = -self.denominator

        except Exception as e:
            print(f"Error while simplifying fraction: {e}")
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    

# Example usage of the library

# Creating fractions
fraction1 = Fraction(4, -8)
fraction2 = Fraction(5, 6)

print("Fraction 1:", fraction1)
print("Fraction 2:", fraction2)