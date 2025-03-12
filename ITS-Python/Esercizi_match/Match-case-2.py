gender:str = input("Inserire il tuo genre: m o f ")
name:str = input("Inserire il tuo nome: ") 

match gender:
    case "m":
        print(f"Nome: {name}\nGenere: Maschio")
    case "f":
        print(f"Nome: {name}\nGenere: Femmina")
    case _:
        print("Errore non è possibile stampare un documento con questi dati")
    