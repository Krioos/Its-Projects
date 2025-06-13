def is_valid_ipv4(address: str) -> bool:
    """
    Determina se una stringa rappresenta un indirizzo IPv4 valido.
    """
    lista: list[str] = address.split('.')
    if len(lista) != 4:
        return False
    for elem in lista:
        for number in elem:
            if not number.isdigit():
                return False
        if not (0 <= int(elem) <= 255):
            return False
    return True

print(is_valid_ipv4("192.168.0.1")) # True
print(is_valid_ipv4("255.255.255.255")) # True
print(is_valid_ipv4("256.100.10.1")) # False (256 è fuori range)
print(is_valid_ipv4("192.168.1")) # False (solo 3 parti)
print(is_valid_ipv4("192.168.1.a")) # False (parte non numerica)
        
