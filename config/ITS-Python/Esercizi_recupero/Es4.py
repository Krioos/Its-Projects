def verifica(x, y, z)-> str:
    if x and (y or z):
        return "Azione permessa"
    else:
        return "Azione negata"
    

print(verifica(1,0,1))
print(verifica(1,1,0))
print(verifica(0,1,1))