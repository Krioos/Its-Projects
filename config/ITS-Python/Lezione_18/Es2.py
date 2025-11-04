def validate_password(password: str) -> bool:
    special_characters = '"!@#$%^&*()-+?_=,<>/"'
    count_specilas = 0
    uppercase = 0
    for character in password:
        uppercase += 1 if character.isupper() else 0
        count_specilas += 1 if character in special_characters else 0
    if uppercase > 3 and count_specilas >= 4 and len(password) >= 20:
        print(True)
        return True
    else:
        raise ValueError(f"password doesn't meet the criterias")

try: 
    validate_password(input("Insert a password: "))
    print("Password is valid")
except ValueError as e:
    print(f"Invalid password, {e}")
