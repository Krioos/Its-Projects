def vowelRemover(stringa: str) -> str:
    if stringa:
        if stringa[0].lower() in ["a", "e", "i", "o", "u"]:
            return "" + vowelRemover(stringa[1:])
        else:
            return stringa[0] + vowelRemover(stringa[1:])
    else:
        return ""

print(vowelRemover(input("Inserisci una stringa: ")))