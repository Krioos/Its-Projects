mammiferi: list[str] = ['cane', 'gatto', 'cavallo', 'elefante', 'leone', 'balena', 'delfino']
rettili: list[str] = ['serpente', 'lucertola', 'tartaruga', 'coccodrillo']
uccelli: list[str] = ['aquila', 'pappagallo', 'gufo', 'falco', 'cigno', 'anatra', 'gallina', 'tacchino']
pesci: list[str] = ['squalo', 'trota', 'salmone', 'carpa']

animale: str = input("Inserire un animale: ").strip().lower()
habitat: str = input("Inserire un habitat (Acqua, Aria, Terra): ").strip().lower()

match animale:
    case animale if animale in mammiferi:
        animal_type = "mammifero"
        print(f"{animale} appartiene alla categoria dei mammiferi")
    case animale if animale in rettili:
        animal_type = "rettile"
        print(f"{animale} appartiene alla categoria dei rettili")
    case animale if animale in uccelli:
        animal_type = "uccello"
        print(f"{animale} appartiene alla categoria degli uccelli")
    case animale if animale in pesci:
        animal_type = "pesce"
        print(f"{animale} appartiene alla categoria dei pesci")
    case _:
        animal_type = "unknown"
        print(f"Impossibile classificare {animale}")

animal_dict: dict = {"animale": animale,
                     "animal type": animal_type,
                     "habitat": habitat}

match (animal_type, habitat):
    case ("mammifero", habitat) if habitat != "aria":
        match (animale, habitat):
            case ("delfino", "acqua") | ("balena", "acqua"):
                print(f"L'animale {animale} può vivere nell'habitat {habitat}")
            case (_, "acqua"):
                print(f"L'animale {animale} non può vivere nell'habitat {habitat}")
            case _:
                print(f"L'animale {animale} può vivere nell'habitat {habitat}")
    case ("mammifero", "aria"):
        print(f"L'animale {animale} non può vivere nell'habitat {habitat}")
    case ("rettile", habitat) if habitat != "aria":
        match (animale, habitat):
            case (_, "acqua") if animale not in {"coccodrillo", "tartaruga"}:
                print(f"L'animale {animale} non può vivere nell'habitat {habitat}")
            case _:
                print(f"L'animale {animale} può vivere nell'habitat {habitat}")
    case ("rettile", "aria"):
        print(f"L'animale {animale} non può vivere nell'habitat {habitat}")
    case ("uccello", "aria"):
        if animale in {"gallina", "tacchino"}:
            print(f"L'animale {animale} non può vivere nell'habitat {habitat}")
        else:
            print(f"L'animale {animale} può vivere nell'habitat {habitat}")
    case ("uccello", "acqua"):
        if animale in {"anatra", "cigno"}:
            print(f"L'animale {animale} può vivere nell'habitat {habitat}")
        else:
            print(f"L'animale {animale} non può vivere nell'habitat {habitat}")
    case ("pesce", "acqua"):
        print(f"L'animale {animale} può vivere nell'habitat {habitat}")
    case ("pesce", _):
        print(f"L'animale {animale} non può vivere nell'habitat {habitat}")
    case _:
        print("Caso non gestito.")
