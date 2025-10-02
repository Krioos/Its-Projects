# esempio di modulus (n) preso da openssl
n_hex = """00:cf:f9:f5:1b:31:5a:2b:6c:a1:8e:28:e8:86:cb:
    4c:26:ee:0e:3b:23:f0:aa:f6:fe:29:46:a9:86:04:
    61:c3:28:4f:8e:fd:53:4d:12:b7:5f:6c:66:7d:9b:
    a8:51:1b:18:ac:e5:35:27:b0:2d:67:65:bf:de:a1:
    11:cb:3a:94:dc:c8:9d:50:e1:95:5a:5c:7c:4d:66:
    e0:57:c1:3a:32:fd:90:8b:a1:6e:74:24:dc:9b:91:
    da:9a:62:e5:ea:17:07:f3:28:ca:c5:b6:dd:d5:8e:
    be:bf:ca:95:f0:0e:25:0e:d5:d8:ad:f4:5e:ca:3c:
    95:3a:a0:38:2f:fb:f1:37:d2:01:8c:8d:2d:ea:69:
    10:8f:09:b9:d7:c5:99:94:97:5e:08:99:e8:62:65:
    0f:f7:4d:3b:4e:96:52:e8:3d:98:14:04:4a:79:7f:
    c1:d6:ac:d8:cb:ca:b7:d3:6b:99:d2:3e:05:85:72:
    02:2b:6b:f3:58:81:59:d0:c6:28:95:fb:44:01:27:
    38:62:55:e9:95:4d:97:60:bb:36:76:bc:1f:5d:4a:
    47:9c:1a:ca:1c:28:ba:f0:5a:3c:21:1a:6f:18:ac:
    5d:1a:6d:74:e9:6c:7e:5e:4e:e8:24:97:fe:6f:01:
    26:d7:ad:85:b2:52:77:8a:1f:60:45:b4:b8:96:35:
    ac:d9
"""  

# pulizia stringa
n_hex = n_hex.replace(":", "").replace("\n", "").replace(" ", "")

# conversione in intero
n = int(n_hex, 16)

# esponente pubblico
e = 3

# esponente privato (anche lui da convertire come sopra)
d_hex = """0d:dd:76:bd:8b:d2:cf:b1:e8:a3:13:cb:3c:2f:af:
    be:54:23:15:02:65:60:bb:22:02:c0:71:b3:99:e4:
    62:58:05:4d:cc:9f:27:45:83:b1:07:3a:08:5f:b5:
    e3:46:12:b6:31:69:f1:94:47:4b:28:ea:a8:71:23:
    51:d0:b4:97:40:93:05:64:5f:4a:4a:6e:af:d3:a8:
    8e:62:37:14:77:4d:e7:2c:e5:3a:f1:64:0a:5f:0e:
    92:d3:64:a9:34:bc:43:69:1e:95:b6:db:96:c5:3f:
    ea:a7:1b:10:00:f1:67:63:96:fa:87:c2:0d:7b:81:
    6a:4e:f2:ad:dd:98:9d:52:25:92:a7:2b:7d:42:33:
    04:bc:da:3e:41:a5:1f:ab:27:e3:5d:98:a6:4b:10:
    1b:97:fb:44:fa:fa:c9:4b:42:1c:13:5c:1b:65:dd:
    69:90:b9:51:ed:f9:56:35:30:d2:4a:7e:3f:0c:ac:
    c0:8b:a5:87:6e:0e:b7:0f:28:59:71:d1:ae:b7:fd:
    59:3c:9d:d1:e4:7b:c2:e3:b9:ba:00:41:15:85:2f:
    64:e0:4f:22:71:01:53:2c:45:24:38:77:f9:0f:04:
    8a:28:5c:86:b2:bb:06:4a:12:b7:62:19:b4:97:07:
    7d:21:82:96:3c:09:5a:1d:a2:36:c1:66:3d:11:79:
    c7
"""
d_hex = d_hex.replace(":", "").replace("\n", "").replace(" ", "")
d = int(d_hex, 16)


msg = "ciao"

# convertilo in numero intero
M = int(msg.encode().hex(), 16)

# cifratura
C = pow(M, e, n)

# decifratura
M_dec = pow(C, d, n)

# riconverti il numero in bytes
M_bytes = M_dec.to_bytes((M_dec.bit_length() + 7) // 8, "big")
print(M_bytes.decode())


numero =  8735
with open("numero.txt", "wb") as f:
    f.write(numero.to_bytes(4, "big"))


def primes_up_to(n: int) -> list[int]:
    result = []
    if n < 2:
        return result
    else:
        prime = True
        for i in range(2, n+1):
            for j in range(2, i+1):
                if i % j == 0:
                    prime = False
                    break
        if prime:
            result.append(i)
    return result
                