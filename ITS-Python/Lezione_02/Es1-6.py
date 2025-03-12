menu :dict = {"Pizza": 9.00,

"Pasta": 10.50,

"Zuppa" : 7.00,

"Hamburger": 15.50,

"Cotoletta": 10.00,

"Salmone": 20.20,

"Patatine Fritte": 5.50,

"Patate al forno": 5.50,

"Verdura del giorno": 7.00,

"Cheesecake": 6.00,

"Tiramisu'": 6.00,

"Focaccia con Nutella": 6.00,

"Coca Cola": 3.50,

"Acqua": 1.50,

"Vino": 5.00
}

ordine: dict = {}

scelta = input("""Scegliere una cosa da prendere dal menù, l'ordine 
               deve comprendere almeno:
               un primo, un secondo, un contorno, una bevanda ed un dolce.
               Sceglire esci per terminare.
               """)
while scelta != "esci":
    ordine[scelta] = menu[scelta]
    scelta = input("""Scegliere una cosa da prendere dal menù, l'ordine 
               deve comprendere almeno:
               un primo, un secondo, un contorno, una bevanda ed un dolce.
               Sceglire esci per terminare.
               """)

sum = 0
for i in ordine.values():
     sum += i

print("Il cliente ha ordinato ", end  = "")
for i in ordine.keys():
     print(f"{i}, ", end = "")
     

print(f"per un totale di {sum}€")