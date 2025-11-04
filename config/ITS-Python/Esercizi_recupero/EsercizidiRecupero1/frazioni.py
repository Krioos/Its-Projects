class Frazione:
    def __init__(self, numeratore: int | float | str, denominatore: int | float | str) -> None:
        self.numeratore = numeratore
        self.denominatore = denominatore

    @property
    def numeratore(self) -> int:
        return self._numeratore

    @numeratore.setter
    def numeratore(self, value: int | float | str) -> None:
        try:
            self._numeratore = int(float(value))
        except:
            print("Valore numeratore non valido, assegnazione default = 13")
            self._numeratore = 13

    @property
    def denominatore(self) -> int:
        return self._denominatore

    @denominatore.setter
    def denominatore(self, value: int | float | str) -> None:
        try:
            val = int(float(value))
            if val == 0:
                raise ValueError("Denominatore non può essere zero")
            self._denominatore = val
        except:
            print("Valore denominatore non valido o zero, assegnazione default = 5")
            self._denominatore = 5

    def value(self) -> float:
        return round(self.numeratore / self.denominatore, 3)

    def __str__(self) -> str:
        return f"{self.numeratore}/{self.denominatore}"


def mcd(x: int, y: int) -> int:
    x = abs(int(x))
    y = abs(int(y))
    while y:
        x, y = y, x % y
    return x


def semplifica(lista: list[Frazione]) -> list[Frazione]:
    out_list = []
    for fraction in lista:
        fattore = mcd(fraction.numeratore, fraction.denominatore)
        semplificata = Frazione(fraction.numeratore // fattore, fraction.denominatore // fattore)
        out_list.append(semplificata)
    return out_list


def fractionCompare(list1: list[Frazione], list2: list[Frazione]) -> None:
    for f1, f2 in zip(list1, list2):
        print(f"Valore frazione originale: {str(f1)} - Valore frazione semplificata: {str(f2)}")

def initialize_list(lista: list[str]) -> list[Frazione]:
    out_list = []
    for elem in lista:
        try:
            num, den = elem.split("/")
            out_list.append(Frazione(num, den))
        except:
            print(f"Errore nel parsing di '{elem}', saltato.")
    return out_list



lista = ["2.5/0", "1/2", "2/4", "3/5", "6/9", "4/7", "24/36", "12/36", "40/60", "5/11", "10/45", "42/78", "9/15"]
l = initialize_list(lista)
l_s = semplifica(l)
fractionCompare(l, l_s)
