from Persona import Person

# persona è definita superclasse o calsse padre
# la classe studente è sottoclasse o derivata di persona
# quindi la classe studente eredita tutta i metodi della classe persona
class Student(Person):
    def __init__(self, name, lastname, age):
        super().__init__(name, lastname, age)
