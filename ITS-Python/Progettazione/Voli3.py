from typing import Self

class IntGEZ(int):
    def __new__(cls, value: Self | int | float | str | bool) -> Self:
        try:
            int_value = int(value)
        except ValueError:
            raise ValueError("Il valore deve essere convertibile in un intero.")
        if int_value < 0:
            raise ValueError("Il valore deve essere un intero maggiore o uguale a zero.")
        return super().__new__(cls, int_value)

class IntGZ(int):
    def __new__(cls, value: Self | int | float | str | bool) -> Self:
        try:
            int_value = int(value)
        except ValueError:
            raise ValueError("Il valore deve essere convertibile in un intero.")
        if int_value <= 0:
            raise ValueError("Il valore deve essere un intero maggiore di zero.")
        return super().__new__(cls, int_value)

class IntG1900(int):
    def __new__(cls, value: Self | int | float | str | bool) -> Self:
        try:
            int_value = int(value)
        except ValueError:
            raise ValueError("Il valore deve essere convertibile in un intero.")
        if int_value < 1900:
            raise ValueError("Il valore deve essere un intero maggiore o uguale a 1900.")
        return super().__new__(cls, int_value)




class Nazione:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    @property
    def nome(self) -> str:
        return self._name

    @nome.setter
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
    def __init__(self, nome: str, abitanti: IntGEZ) -> None:
        self.nome = nome
        self.abitanti = abitanti

    @property
    def nome(self) -> str:
        return self._name

    @nome.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("Il nome della città non può essere vuoto.")
        self._name = value

    @property
    def abitanti(self) -> IntGEZ:
        return self._abitanti

    @abitanti.setter
    def abitanti(self, value: IntGEZ) -> None:
        self._abitanti = check_type(value, IntGEZ)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Citta) and self._name == other._name and self._abitanti == other._abitanti

    def __hash__(self) -> int:
        return hash((self._name, self._abitanti))

    def __repr__(self) -> str:
        return f"Citta(name={self._name}, abitanti={self._abitanti})"


class Aeroporto:
    def __init__(self, codice: str, nome: str) -> None:
        self._codice = codice
        self.nome = nome
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
    def __init__(self, codice: str, durata_minuti: int | IntGZ) -> None:
        self._codice = codice
        self.durata_minuti = durata_minuti

    @property
    def codice(self) -> str:
        return self._codice

    @property
    def durata_minuti(self) -> IntGZ:
        return self._durata_minuti

    @durata_minuti.setter
    def durata_minuti(self, value: int | IntGZ) -> None:
        self._durata_minuti = check_type(value, IntGZ)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Volo) and self._codice == other._codice

    def __hash__(self) -> int:
        return hash(self._codice)

    def __repr__(self) -> str:
        return f"Volo(codice={self._codice}, durata_minuti={self._durata_minuti})"


class CompagniaAerea:
    def __init__(self, nome: str, anno_fondazione: int | IntG1900) -> None:
        self.nome = nome
        self._anno_fondazione = anno_fondazione

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
