def xor_chiper(s:str, key:int)-> list[int]:
    return [ord(char) ^ key for char in s]

def xor_dechiper(lista:list[int], key:int)-> str:
    result: str = ""
    for elem in lista:
        result += chr(elem ^ key)
    return result

stringa = input("Inserire la stringa da cifrare: ")
key = int(input("Inserie la chiave: "))
result = xor_chiper(stringa, key)
print(result)
print(xor_dechiper(result, key))



from functools import reduce


msg = input("Dammi il messaggio: ")
key = int(input("Dammi la chiave: "))

cifrato = [ord(c)^key for c in msg]
# la precedente può essere scritta come un for semplice
cifrato=[]
for c in msg:
    cifrato.append(ord(c)^key)

print("Messaggio cifrato: ", cifrato)

# Ora decifro

#Uso la comprhension
decifrato = ''.join([chr(c^key) for c in cifrato])
# la precedente può essere scritta come un for semplice
decifrato = []
for c in cifrato:
    decifrato.append(chr(c^key))
decifrato = ''.join(decifrato)
print("Messaggio decifrato: ", decifrato)
# Nota: join è un metodo delle stringhe, non una funzione globale
# Quindi non posso fare join(cifrato) ma devo fare ''.join(cifrato)
# oppure usare join(cifrato) se cifrato è una lista di stringhe
# oppure ''.join(cifrato) se cifrato è una lista di caratteri
# oppure ''.join(map(chr, cifrato)) se cifrato è una lista di interi

#In un altro modo, usando map e reduce
cifrato = list(map(lambda c: ord(c) ^ key, msg))
print("Messaggio cifrato: ", cifrato)

decifrato = reduce(lambda x,y: x+y, map(lambda x : chr(x ^ key), cifrato), "")
print("Messaggio decifrato: ", decifrato)

# la map trasforma una lista in un'altra lista consentendo di modificare gli elementi
l=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: x*3, l)))
print(list(map(lambda x: x*x, l)))
# data la lista l intendo sommare tutti gli elementi tra loro
print(reduce(lambda x,y: x+y, l, 0))