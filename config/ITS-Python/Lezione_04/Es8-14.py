def make_car( car_brand, car_model, **arguments):
    return {"Brand": car_brand, "Model" : car_model, **arguments}

car = make_car("subaru", "outback", color = "blue", tow_package = True)
print(car)