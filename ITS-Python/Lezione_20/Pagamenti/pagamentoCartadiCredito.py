from pagamento import Pagamento

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, importo:float, nome:str, data_scadenza:str, numero_carta:str)-> None:
        self.setImporto(importo)
        self.setNome(nome)
        self.setDataScadenza(data_scadenza)
        self.setNumeroCarta(numero_carta)
    
    def setNome(self, value:str)-> None:
        if isinstance(value, str):
            self.__nome = value
        else:
            print("Errore il valore non è corretto")
    
    def setDataScadenza(self, value:str)-> None:
        if isinstance(value, str):
            self.__data_scadenza = value
        else:
            print("Errore il valore non è corretto")
    
    def setNumeroCarta(self, value:str)-> None:
        if isinstance(value, str):
            self.__numero_carta = value
        else:
            print("Errore il Valore non è corretto")
        
    def getNome(self)-> str | None:
        try:
            return self.__nome
        except Exception:
            return None
    
    def getDataScadenza(self)-> str | None:
        try:
            return self.__data_scadenza
        except Exception:
            return None
    
    def getNumeroCarta(self)-> str | None:
        try:
            return self.__numero_carta
        except Exception:
            return None
    
    def dettagliPagamento(self):
        s = super().dettagliPagamento() + " pagamento con carta\n"
        return s + f"""
Nome sulla carta: {self.getNome()}
Data di scadenza: {self.getDataScadenza()}
Numero della carta: {self.getNumeroCarta()}\n"""