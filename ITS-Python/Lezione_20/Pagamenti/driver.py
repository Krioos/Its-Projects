from pagamento_contanti import PagamentoContanti
from pagamentoCartadiCredito import PagamentoCartaDiCredito


pagamentoContanti_1 = PagamentoContanti(150.00)
pagamentoContanti_2 = PagamentoContanti(95.25)

print(pagamentoContanti_1.dettagliPagamento())
print(pagamentoContanti_2.dettagliPagamento())


pagamentoCarta_1 = PagamentoCartaDiCredito(200.00, "Mario Rossi", "12/24", "1234567890123456")
pagamentoCarta_2 = PagamentoCartaDiCredito(500.00, "Luigi Bianchi", "01/25", "6543210987654321")
print(pagamentoCarta_1.dettagliPagamento())
print(pagamentoCarta_2.dettagliPagamento())