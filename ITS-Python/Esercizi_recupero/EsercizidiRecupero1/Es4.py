def isDNA(stringa: str)-> bool:
    legal_characters = ["A", "C", "G", "T"]
    for character in stringa: 
        if character not in legal_characters:
            return False
    return True

s1= "TTGACCAGGTCA"
s2= "AACCGGTTAA"
s3 = "Casa"

print(f"{isDNA(s1)}\n{isDNA(s2)}\n{isDNA(s3)}")