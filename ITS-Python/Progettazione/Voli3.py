class IntGEZ(int):
    def __new__(cls, value: int) -> object:
        if value < 0:
            raise ValueError("Il valore deve essere un intero maggiore o uguale a zero.")
        return super().__new__(cls, value)

class IntGZ(int):
    def __new__(cls, value: int) -> object:
        if value <= 0:
            raise ValueError("Il valore deve essere un intero maggiore di zero.")
        return super().__new__(cls, value)

class IntG1900(int):
    def __new__(cls, value: int) -> object:
        if value < 1900:
            raise ValueError("Il valore deve essere un intero maggiore o uguale a 1900.")
        return super().__new__(cls, value)

class Nazione:
    def __new__(cls, name: str) -> object:
        if not name:
            raise ValueError("Il nome della nazione non può essere vuoto.")
        return super().__new__(cls)
    
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("Il nome della nazione non può essere vuoto.")
        self._name = value

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Nazione) and self._name == other._name

    def __hash__(self) -> int:
        return hash(self._name)

    def __repr__(self) -> str:
        return f"Nazione({self._name})"


class Citta:
    def __new__(cls, name: str, abitanti: IntGEZ) -> object:
        if not name:
            raise ValueError("Il nome della città non può essere vuoto.")
        if not isinstance(abitanti, IntGEZ):
            raise TypeError("Il numero di abitanti deve essere un intero maggiore o uguale a zero.")
        return super().__new__(cls)

    def __init__(self, name: str, abitanti: IntGEZ) -> None:
        self._name = name
        self._abitanti = abitanti

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("Il nome della città non può essere vuoto.")
        self._name = value

    @property
    def abitanti(self) -> IntGEZ:
        return self._abitanti

    @abitanti.setter
    def abitanti(self, value: IntGEZ) -> None:
        if not isinstance(value, IntGEZ):
            raise TypeError("Il numero di abitanti deve essere un intero maggiore o uguale a zero.")
        self._abitanti = value

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Citta) and self._name == other._name and self._abitanti == other._abitanti

    def __hash__(self) -> int:
        return hash((self._name, self._abitanti))

    def __repr__(self) -> str:
        return f"Citta(name={self._name}, abitanti={self._abitanti})"

class Aeroporto:
    def __new__(cls, codice: str, nome: str) -> object:
        if not codice or not nome:
            raise ValueError("Il codice e il nome dell'aeroporto non possono essere vuoti.")
        return super().__new__(cls)

    def __init__(self, codice: str, nome: str) -> None:
        self._codice = codice
        self._nome = nome

    @property
    def codice(self) -> str:
        return self._codice

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, value: str) -> None:
        if not value:
            raise ValueError("Il nome dell'aeroporto non può essere vuoto.")
        self._nome = value

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Aeroporto) and self._codice == other._codice

    def __hash__(self) -> int:
        return hash(self._codice)

    def __repr__(self) -> str:
        return f"Aeroporto(codice={self._codice}, nome={self._nome})"


class Volo:
    def __new__(cls, codice: str, durata_minuti: IntGZ) -> object:
        if not codice:
            raise ValueError("Il codice del volo non può essere vuoto.")
        if not isinstance(durata_minuti, IntGZ):
            raise TypeError("La durata del volo deve essere un intero maggiore di zero.")
        return super().__new__(cls)

    def __init__(self, codice: str, durata_minuti: IntGZ) -> None:
        self._codice = codice
        self._durata_minuti = durata_minuti

    @property
    def codice(self) -> str:
        return self._codice

    @property
    def durata_minuti(self) -> IntGZ:
        return self._durata_minuti

    @durata_minuti.setter
    def durata_minuti(self, value: IntGZ) -> None:
        if not isinstance(value, IntGZ):
            raise TypeError("La durata del volo deve essere un intero maggiore di zero.")
        self._durata_minuti = value

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Volo) and self._codice == other._codice

    def __hash__(self) -> int:
        return hash(self._codice)

    def __repr__(self) -> str:
        return f"Volo(codice={self._codice}, durata_minuti={self._durata_minuti})"


class CompagniaAerea:
    def __new__(cls, nome: str, anno_fondazione: IntG1900) -> object:
        if not nome:
            raise ValueError("Il nome della compagnia aerea non può essere vuoto.")
        if not isinstance(anno_fondazione, IntG1900):
            raise TypeError("L'anno di fondazione deve essere un intero maggiore o uguale a 1900.")
        return super().__new__(cls)

    def __init__(self, nome: str, anno_fondazione: IntG1900) -> None:
        self._nome = nome #id mutabile
        self._anno_fondazione = anno_fondazione # immutabile

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, value: str) -> None:
        if not value:
            raise ValueError("Il nome della compagnia aerea non può essere vuoto.")
        self._nome = value

    @property
    def anno_fondazione(self) -> IntG1900:
        return self._anno_fondazione

    def __eq__(self, other: object) -> bool:
        return isinstance(other, CompagniaAerea) and self._nome == other._nome

    def __hash__(self) -> int:
        return hash(self._nome)

    def __repr__(self) -> str:
        return f"CompagniaAerea(nome={self._nome}, anno_fondazione={self._anno_fondazione})"


