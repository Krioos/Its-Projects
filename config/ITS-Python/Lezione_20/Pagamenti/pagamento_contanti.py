from pagamento import Pagamento

class PagamentoContanti(Pagamento):

    def __init__(self, importo:float)-> None:
        self.setImporto(importo)
    
    def inPezziDa(self) -> str:
        try:
            importo = self.getImporto()
            value = int(round(importo * 100))
            tagli = [
                ("500€", 50000),
                ("200€", 20000),
                ("100€", 10000),
                ("50€", 5000),
                ("20€", 2000),
                ("10€", 1000),
                ("5€", 500),
                ("2€", 200),
                ("1€", 100),
                ("0,50€", 50),
                ("0,20€", 20),
                ("0,10€", 10),
                ("0,05€", 5),
                ("0,01€", 1),
            ]

            risultato = []
            for nome, valore in tagli:
                pezzi, value = divmod(value, valore)
                if pezzi > 0:
                    risultato.append((pezzi, nome))
            result_str = f"Importo totale: {importo:.2f}€\n"
            for pezzi, nome in risultato:
                result_str += f"{pezzi} x {nome}\n"
            return result_str.strip()
        except Exception:
            return "Il valore di importo non è definito"
    def dettagliPagamento(self):
        s = super().dettagliPagamento() + " pagamento in contanti\n"
        return s + self.inPezziDa()
