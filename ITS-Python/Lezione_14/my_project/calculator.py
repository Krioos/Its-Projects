class Calculator():
    def __init__(self, a: int, b: int)-> None:
        self._a = a
        self._b = b
    
    @property
    def a(self)-> int:
        return self._a
    @property
    def b(self)-> int:
        return self._b
    
    def addition(self)-> int:
        return int(self.a + self.b)

    def subtraction(self) -> int:
        return int(self.a - self.b)
    
    def multiplication(self) -> int:
        return int(self.a * self.b)
    
    def division(self)-> float | None:
        try:
            return round(self.a / self.b, 2)
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")