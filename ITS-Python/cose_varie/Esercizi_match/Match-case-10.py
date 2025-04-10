stringa:str = input("Inserire una stringa: ")

lista_str = [carattere for carattere in stringa]

match lista_str:
    case[*_, "?"] if len(lista_str) % 2 == 0:
        print("Sì")
    case[*_,"?"] if len(lista_str) % 2 != 0:
        print("No")
    case[*_, "!"]:
        print("Wow")
    case _:
        print(f"Tu dici {stringa}")
