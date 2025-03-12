def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += new_char
        else:
            result += char
    return result

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)


def xor_hex(hex_string, key):
    hex_bytes = bytes.fromhex(hex_string)
    xor_result = bytes(b ^ key for b in hex_bytes)
    return xor_result.hex()