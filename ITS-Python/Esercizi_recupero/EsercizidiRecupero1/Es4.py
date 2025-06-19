def isDNA(stringa: str)-> bool:
    legal_characters = ["A", "C", "G", "T"]
    for character in stringa: 
        if character not in legal_characters:
            return False
    return True

def comparisonDNA(dna1:str, dna2:str)-> None:
    if isDNA(dna1) and isDNA(dna2):
        max_len:int  = max(len(dna1), len(dna2))
        for i in range(max_len, 0, -1):
            if dna1[-i:] == dna2[:i]:
               overlap = i
               break
        if overlap != 0:
            print(f"{dna1}\n{' ' * (len(dna1) - overlap)}{dna2}")
            print(f"La massima lunghezza di sovrapposizione è {overlap}")
        else:
            print("Le due seguenza di DNA non sono sovrapponibili")
    else:
        print("Una delle due seguenza non è corretta")

s1= "TTGACCAGGTCA"
s2= "AACCGGTTAA"

comparisonDNA(s1,s2)

s1= "GGTACCGTGA"
s2= "CGTGAACCTT"

comparisonDNA(s1, s2)

s1= "AAGCTTACG"
s2= "ACGTTCGA"

comparisonDNA(s1, s2)