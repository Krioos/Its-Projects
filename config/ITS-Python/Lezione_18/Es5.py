class FormulaError(Exception):
    pass

def calculator() -> None:
    formula = ""
    while True:
        formula = input("Insert a formula separated by white spaces (quit to finish): ").lower()
        if formula == "quit":
            return
        
        else:
            formula = formula.split()

        try:
            if len(formula) != 3:
                raise FormulaError("The formula must have exactly three elements.")
            try:
                value1 = float(formula[0])
                value2 = float(formula[2])
            except ValueError:
                raise FormulaError("One of the nubmers is not valid")
            
            if formula[1] not in ["+", "-"]:
                raise FormulaError("The operator must be + or - only")

        except FormulaError as e:
            print(f"Error {e}")
            continue
        else:
            if formula[1] == "+":
                print(f"Result: {value1 + value2}")
            else:
                print(f"Result: {value1 - value2}")
calculator()