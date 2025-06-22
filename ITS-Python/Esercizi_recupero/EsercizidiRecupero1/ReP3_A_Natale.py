from random import randint
class Creatura():
    def __init__(self, nome:str)-> None:
        self.setNome(nome)

    def getNome(self) -> str:
        return self.__nome
    
    def setNome(self, nome:str) -> None:
        if isinstance(nome, str):
            self.__nome = nome
        else:
            self.__nome = "Creatura Generica"
    
    def __str__(self) -> str:
        return f"Creatura: {self.getNome()}"


class Alieno(Creatura):
    def __init__(self, nome:str)-> None:
        self.__setMatricola()
        self.__setMunizioni()
        nome_atteso = "Robot-" + str(self.getMatricola())
        if nome + str(self.getMatricola()) != nome_atteso:
            print('Attenzione! Tutti gli Alieni devono avere il nome "Robot" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!')
            nome = nome_atteso
        self.setNome(nome_atteso)
    
    def getMatricola(self) -> int:
        return self.__matricola
    
    def __setMatricola(self) -> None:
        self.__matricola: int = randint(1*10000, 9*10000)

    def getMunizioni(self) -> list[int]:
        return self.__munizioni

    def __setMunizioni(self)-> None:
        self.__munizioni:list[int] = [i**2 for i in range(15)]
    
    def __str__(self)-> str:
        return f"Alieno: {self.getNome()}"
    
    def __repr__(self) -> str:
        return f"Alieno: {self.getNome()}\nMunizioni: {self.getMunizioni()}"
    
    
class Mostro(Creatura):
    urlo_vittoria: str = "GRAAAHHH"
    gemito_sconfitta: str = "Uuurghhh"

    def __init__(self, nome:str, urlo_vittoria:str, gemito_sconfitta:str)-> None:
        super().__init__(nome)
        self.__setAssalto()
        self.__setUrloVittoria(urlo_vittoria)
        self.__setGemitoSconfitta(gemito_sconfitta)

    
    def getAssalto(self) -> list[int]:
        return self.__assalto
    
    def __setAssalto(self)-> None:
        self.__assalto:list[int] = [randint(1,100) for _ in range(15)]
    
    def getUrloVittoria(self) -> str:
        return self.__urlo_vittoria
    
    def __setUrloVittoria(self, value)-> None:
        if isinstance(value, str):
            self.__urlo_vittoria = value
        else:
            self.__urlo_vittoria = Mostro.urlo_vittoria
    
    def getGemitoSconfitta(self) -> str:
        return self.__gemito_sconfitta
    
    def __setGemitoSconfitta(self, value)-> None:
        if isinstance(value, str):
            self.__gemito_sconfitta = value
        else:
            self.__gemito_sconfitta = Mostro.gemito_sconfitta
    

    def __str__(self) -> str:
        result = self.getNome().lower()
        for i in range(len(result)):
            if i % 2 != 0:
                result = result[:i] + result[i].upper() + result[i+1:]
        return f"Mostro: {result}"
    
    def __repr__(self) -> str:
        return f"Mostro: {self.getNome()}\nAssalto: {self.getAssalto()}"


def pariUguali(a:list[int], b:list[int]) -> list[int]:
    return [1 if a[i]% 2 == 0 and b[i]% 2 == 0 else 0 for i in range (min(len(a), len(b)))]

def combattimento(a: Alieno, m: Mostro)-> None | Alieno | Mostro:
    if not isinstance(a, Alieno):
        print("Il primo combattente non è un Alieno!")
        return None
    elif not isinstance(m, Mostro):
        print("Il secondo combattente non è un Mostro!")
        return None

    else:
        print("Combattimento")
        esito = pariUguali(a.getMunizioni(), m.getAssalto())
        if esito.count(1) > 4:
            vincitore = m
            for _ in range(3):
                print(m.getUrloVittoria())
        else:
            vincitore = a
            for _ in range(3):
                print(m.getGemitoSconfitta())

    return vincitore

def proclamaVincitore(c:Creatura)-> None:
    testo = str(c)
    larghezza = len(testo) + 10
    altezza = 5
    if isinstance(c, Alieno):
        print("Gli Alieni hanno vinto!")
    else:
        print("I Mostri hanno vinto!")

    for i in range(altezza):
        if i == 0 or i == altezza - 1:
            print("*" * larghezza)
        elif i == 2:
            print("*", end="")
            print(" " * 2, end="")
            print(c, end="")
            spazi_rimanenti = larghezza - 3 - len(str(c))
            print(" " * spazi_rimanenti + "*")
        else:
            print("*" + " " * (larghezza - 2) + "*")


def main():
    alieno = Alieno("Robot-")
    mostro = Mostro("Gorthor", "GRAAAHHH", "Uuurghhh")
    print(repr(alieno))
    print(repr(mostro))
    vincitore = combattimento(alieno, mostro)
    if vincitore:
        proclamaVincitore(vincitore)

