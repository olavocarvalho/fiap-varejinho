from eletronicos import Eletronicos
from vestuario import Vestuario
from gestor_loja import GestorLoja
from estoque import Estoque
from vendas import Vendas
from relatorios import Relatorios
from strategy import DescontoPercentual, DescontoValorFixo

# Configuração do sistema com injeção de dependências
estoque = Estoque()
vendas = Vendas(estoque)
relatorios = Relatorios(vendas, estoque)

# Instanciação do GestorLoja
gestor = GestorLoja(estoque, vendas, relatorios)

# Criando produtos
produto1 = Eletronicos("Smartphone", "001", 10, 1500.00, "Smartphone de última geração", "Fornecedor A")
produto2 = Vestuario("Camiseta", "002", 20, 50.00, "Camiseta de algodão", "Fornecedor B")
produto3 = Eletronicos("Laptop", "003", 5, 3000.00, "Laptop de alto desempenho", "Fornecedor C")
produto4 = Vestuario("Calça Jeans", "004", 8, 100.00, "Calça Jeans Masculina", "Fornecedor D")

# Adicionando ao estoque
print(gestor.adicionar_produto(produto1))
print(gestor.adicionar_produto(produto2))
print(gestor.adicionar_produto(produto3))
print(gestor.adicionar_produto(produto4))

# Atualizando o estoque (simulação de alteração na quantidade manualmente)
print(gestor.atualizar_produto("001", 15))  # Aumentando o estoque de Smartphone

# Removendo um produto do estoque
print(gestor.remover_produto("002"))  # Removendo a Camiseta

# Registrando vendas
# Venda 1: 2 Smartphones com 10% de desconto
desconto_percentual = DescontoPercentual(10)
print(gestor.registrar_venda("001", 2, desconto_percentual))

# Venda 2: 3 Laptops sem desconto
print(gestor.registrar_venda("003", 3))

# Venda 3: 6 Calças Jeans, sem desconto (para testar alerta de estoque baixo)
print(gestor.registrar_venda("004", 6))

# Relatórios
print("\nRelatório de Vendas:")
print(gestor.gerar_relatorio_vendas())

print("\nRelatório de Estoque:")
print(gestor.gerar_relatorio_estoque())

print("\nHistórico de Movimentação:")
print(gestor.gerar_historico_movimentacao())

# Alertas de estoque
print("\nAlertas de Estoque:")
alertas = gestor.verificar_alertas_estoque()
for alerta in alertas:
    print(alerta)