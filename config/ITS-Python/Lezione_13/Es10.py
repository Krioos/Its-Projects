def charDuplicator(stringa:str) -> str:
    if stringa:
        return stringa[0]*2 + charDuplicator(stringa[1:])
    else:
        return ""
    
print(charDuplicator(input("Inserisci una stringa: ")))