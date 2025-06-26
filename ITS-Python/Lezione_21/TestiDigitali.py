class Documento:
    def __init__(self, testo: str)-> None:
        self.setText(testo)

    def getText(self)-> str:
        return self.__testo
    
    def setText(self, value:str)-> None:
        self.__testo = value
    
    def isInText(self, value:str)-> bool:
        if self.getText().find(value) != -1:
            return True
        else:
            return False
    
class Email(Documento):
    def __init__(self, testo:str, titolo:str, mittente:str, destinatario:str)-> None:
        super().__init__(testo)
        self.setTitolo(titolo)
        self.setMittente(mittente)
        self.setDestinatario(destinatario)
    
    def setTitolo(self, value:str)-> None:
        self.__titolo = value
    
    def getTitolo(self)-> str:
        return self.__titolo
    
    def setMittente(self, value:str)-> None:
        self.__mittente = value

    def getMittente(self)-> str:
        return self.__mittente
    
    def setDestinatario(self, value:str)-> None:
        self.__destinatario = value

    def getDestinatario(self)-> str:
        return self.__destinatario

    def getText(self)-> str:
        return f"Da: {self.getMittente()}, A: {self.getDestinatario()}\
            \nTitolo: {self.getTitolo()}\
            \nMessaggio: {super().getText()}"

    def writeToFile(self, path)-> None:
        with open(path, "w") as file:
            file.write(self.getText())

class File(Documento):
    def __init__(self, nomePercorso:str)-> None:
        super().__init__("")
        self.setNomePercorso(nomePercorso)
        self.leggiTestoDaFile()
    
    def getNomePercorso(self)-> str:
        return self.__nomePercorso

    def setNomePercorso(self, value:str)-> None:
        self.__nomePercorso = value
    
    def leggiTestoDaFile(self)-> None:
        with open(self.__nomePercorso, "r") as file:
            text = file.read()
            self.setText(text)
    def getText(self)-> str:
        return f"Percorso: {self.getNomePercorso()}\
            \nContenuto: {super().getText()}"
    
#Test con codice driver

email = Email("incontraci nel path che indicherò dopo",
              "Prova",
              "alice@example.com",
              "bob@example.com")

file = File("/home/its/projects/ITS-Python/Lezione_21/document.txt")

print(email.getText())
print(file.getText())

email.writeToFile("/home/its/projects/ITS-Python/Lezione_21/email1.txt")

assert email.isInText("incontraci") == True, "Assertion Error!"
assert file.isInText("percorso") == False, "Assertion Error!"