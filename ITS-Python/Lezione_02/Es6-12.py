cities: dict = {
    "Rome": {"Country": "Italy", "Population": 2760000, "Fact": "Rome is the capital city of Italy" },
    "Bologna":  {"Country": "Italy", "Population": 392000, "Fact": """In Bologna there's the oldest university of the world.""" },
    "Paris":    {"Country": "France", "Population": 2760000, "Fact": """Paris is the capital city of Fracne.""" },
    "Otranto":  {"Country": "Italy", "Population": 20000, "Fact": """Otranto is the most easterly town of Italy."""},
    "Dublin" :  {"Country": "Ireland", "Population": 200000, "Fact": "Dublin is the capital city of Ireland."}
}
possible_choices = []
working_cities = cities.copy()
print("You have to choose a new city where to live, the following questions will make sure you choose the right city")

flag = False

while not flag:
    country = input("In which country you would like to live? Please choose between Italy, Iralnd or France: ")
    if country not in ["Italy", "France", "Ireland"]:
        print("The selected country is not aveiable, please choose one from Italy, Iralnd or France.")
    else:
        flag = True
        for k,v in cities.items():
            if country != v["Country"]:
                working_cities.pop(k)
flag = False
while not flag:
    people = input("How mucn people should your city have?: ")
    try:
        int(people)

    except:
        raise TypeError("Only numbers please")
    
    finally:
        people = int(people)
        for k,v in working_cities.items():
            if people / 2 <= v["Population"] < people:
                possible_choices.append(k)

        flag = True

print("This cities are the most close to your likings")
if len(possible_choices) == 0:
    print("Sorry no cities are to your likings")
else:
    for elem in possible_choices:
        print(elem)
        for k,v in working_cities[elem].items():
            print(f"{k}:\n{v}")