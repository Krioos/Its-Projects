from custom_types import *
from datetime import date

class Persona:
    _nome: str
    _data_nascita: date
    _cf: str #codice fiscale da fare
    _nascita: date

    _isUomo: bool
    _isDOnna: bool
    _maternita: int | None
    _posizioneMilitare: PosizioneMilitare | None
    
    def __init__(self, nome, data_nascita, nascita, maternita = None, posizioneMilitare = None):
        self.set_nome(nome)
        self.set_dataNascita(data_nascita)
        self.nascita(nascita)
        



class PosizioneMilitare:
    def __init__(self):
        pass