def vowelsCounter(stringa:str) -> int:
    if stringa:
        if stringa[0].lower() in ["a", "e", "i", "o", "u"]:
            return 1 + vowelsCounter(stringa[1:])
        else:
            return 0 + vowelsCounter(stringa[1:])
    else:
        return

print(vowelsCounter(input("Inserisci una stringa: ")))
