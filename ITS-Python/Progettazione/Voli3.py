class IntGEZ(int):
    def __new__(cls, value: int) -> object:
        if value < 0:
            raise ValueError("Il valore deve essere un intero maggiore o uguale a zero.")
        return super().__new__(cls, value)
    
    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"IntGEZ({self.value})"

class IntGZ(int):
    def __new__(cls, value: int) -> object:
        if value <= 0:
            raise ValueError("Il valore deve essere un intero maggiore di zero.")
        return super().__new__(cls, value)
    
    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"IntGZ({self.value})"
    
class IntG1900(int):
    def __new__(cls, value: int) -> object:
        if value < 1900:
            raise ValueError("Il valore deve essere un intero maggiore o uguale a 1900.")
        return super().__new__(cls, value)
    
    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"IntG1900({self.value})"

class Nazione():
    def __new__(cls, name: str)-> object:
        if not name:
            raise ValueError("Il nome della nazione non può essere vuoto.")
        return super().__new__(cls)
    
    def __init__(self, name: str)-> None:
        self.name = name #id

    def __eq__(self, other: object) -> bool:
        if other is None or not isinstance(other, Nazione) or hash(self) != hash(other):
            return False
        else:
            return self.name == other.name
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __repr__(self) -> str:
        return f"Nazione({self.name})"


class Citta():
    def __new__(cls, name: str, abitanti: IntGEZ) -> object:
        if not name:
            raise ValueError("Il nome della città non può essere vuoto.")
        if not isinstance(abitanti, IntGEZ):
            raise TypeError("Il numero di abitanti deve essere un intero maggiore o uguale a zero.")
        return super().__new__(cls)
    
    def __init__(self, name: str, abitanti: IntGEZ) -> None:
        self.name = name 
        self.abitanti = abitanti
    
    def __repr__(self) -> str:
        return f"Citta(name={self.name}, abitanti={self.abitanti})"
    
class Aeroporto():
    def __new__(cls, codice:str, nome: str)-> object:
        if not codice or not nome:
            raise ValueError("Il codice e il nome dell'aeroporto non possono essere vuoti.")
        return super().__new__(cls)
    
    def __init__(self, codice: str, nome: str) -> None:
        self.codice = codice # id
        self.nome = nome

    def __eq__(self, other: object) -> bool:
        if other is None or not isinstance(other, Aeroporto) or hash(self) != hash(other):
            return False
        else:
            return self.codice == other.codice
    
    def __hash__(self) -> int:
        return hash(self.codice)
    
    def __repr__(self) -> str:
        return f"Aeroporto(codice={self.codice}, nome={self.nome})"
    
class Volo():
    def __new__(cls, codice:str, durata_minuti: IntGZ)-> object:
        if not codice:
            raise ValueError("Il codice del volo non può essere vuoto.")
        if not isinstance(durata_minuti, IntGZ):
            raise TypeError("La durata del volo deve essere un intero maggiore di zero.")
        return super().__new__(cls)
    
    def __init__(self, codice: str, durata_minuti: IntGZ) -> None:
        self.codice = codice
        self.durata_minuti = durata_minuti

    def __eq__(self, other: object) -> bool:
        if other is None or not isinstance(other, Volo) or hash(self) != hash(other):
            return False
        else:
            return self.codice == other.codice
    
    def __hash__(self) -> int:
        return hash(self.codice)
    
    def __repr__(self) -> str:
        return f"Volo(codice={self.codice}, durata_minuti={self.durata_minuti})"
    

class CompagniaAerea():
    def __new__(cls, nome: str, anno_fondazione: IntG1900) -> object:
        if not nome:
            raise ValueError("Il nome della compagnia aerea non può essere vuoto.")
        if not isinstance(anno_fondazione, IntG1900):
            raise TypeError("L'anno di fondazione deve essere un intero maggiore o uguale a 1900.")
        return super().__new__(cls)
    
    def __init__(self, nome: str, anno_fondazione: IntG1900) -> None:
        self.nome = nome #id
        self.anno_fondazione = anno_fondazione

    def __eq__(self, other: object) -> bool:
        if other is None or not isinstance(other, CompagniaAerea) or hash(self) != hash(other):
            return False
        else:
            return self.nome == other.nome
        
    def __hash__(self) -> int:
        return hash(self.nome)
    
    def __repr__(self) -> str:
        return f"CompagniaAerea(nome={self.nome}, anno_fondazione={self.anno_fondazione})"
    

