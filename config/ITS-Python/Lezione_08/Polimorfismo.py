#get cancer
from Persona import Person
from Alien import Alien
from Student import Student

# creazione di un oggetto di tipo persona
p: Person = Person("Mario", "Rossi", 30)

# vogliamo visualizzare le informazioni dell'oggetto persona
print(p)

#creaiamo un oggetto di tipo alieno
gimbo: Alien = Alien("Andromeda")

#vogliamo visualizzare le informazioni dell'oggetto alieno
print(gimbo)
# metodo speak per l'oggetto persona
p.speak()
# metodo speak per l'oggetto alieno
gimbo.speak()   

#In questo caso si può notare un esempio di polimorfismo

