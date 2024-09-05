import pyodbc

from infrastructure.repositories.estoque_repository import EstoqueRepository
from infrastructure.repositories.vendas_repository import VendasRepository
from infrastructure.repositories.recibo_repository import ReciboRepository
from infrastructure.repositories.relatorio_repository import RelatorioRepository

from application.service.estoque_service import EstoqueService
from application.service.vendas_service import VendasService
from application.service.recibo_service import ReciboService
from application.service.relatorio_service import RelatorioService

from domain.eletronicos import Eletronicos
from domain.vestuario import Vestuario

# Definindo as classes de modelo, serviço e repositório

# Produto, Eletronicos, Vestuario, Venda, Recibo, Relatorio etc. foram definidos anteriormente.

def main():
    # Conexão ao banco de dados SQL Server
    connection_string = "Driver={ODBC Driver 17 for SQL Server};Server=KARINA;Database=fiapinho;Trusted_Connection=yes;"
    db_conexao = pyodbc.connect(connection_string)

    # Instanciar repositórios
    estoque_repo = EstoqueRepository(db_conexao)
    vendas_repo = VendasRepository(db_conexao)
    recibo_repo = ReciboRepository(db_conexao)  # Caso você queira salvar recibos
    relatorio_repo = RelatorioRepository(db_conexao)  # Caso você queira salvar relatórios

    # Instanciar serviços
    estoque_service = EstoqueService(estoque_repo)
    vendas_service = VendasService(vendas_repo, estoque_service)
    recibo_service = ReciboService(recibo_repo)
    relatorio_service = RelatorioService(vendas_service, estoque_service, relatorio_repo)

    # 1. Adicionar produtos no estoque
    eletronico = Eletronicos(
        nome="Smartphone XYZ",
        codigo="E001",
        quantidade=100,
        preco=1500.00,
        descricao="Smartphone de última geração",
        fornecedor="TechCorp"
    )
    vestuario = Vestuario(
        nome="Camiseta Polo",
        codigo="V001",
        quantidade=200,
        preco=79.90,
        descricao="Camiseta Polo de algodão",
        fornecedor="Textil Brasil"
    )

    # Adiciona produtos no estoque
    print("Adicionando produtos no estoque...")
    estoque_service.adicionar_produto(eletronico)
    estoque_service.adicionar_produto(vestuario)

    # 2. Atualizar um produto no estoque
    print("Atualizando produto no estoque...")
    estoque_service.atualizar_produto("E001", 80)  # Reduzir o estoque do eletrônico

    # 3. Registrar uma venda
    print("Registrando uma venda...")
    resultado_venda = vendas_service.registrar_venda(codigo="E001", quantidade=2)
    print(resultado_venda)

    # 4. Gerar um recibo da venda
    print("Gerando recibo da venda...")
    recibo = recibo_service.gerar_recibo(
        id_venda=1,  # ID da venda gerada
        produto="Smartphone XYZ",
        quantidade=2,
        valor_total=3000.00
    )
    print(recibo)

    # 5. Gerar relatórios
    print("Gerando relatórios...")
    
    # Relatório de vendas
    relatorio_vendas = relatorio_service.relatorio_vendas()
    print(relatorio_vendas)

    # Relatório de estoque
    relatorio_estoque = relatorio_service.relatorio_estoque()
    print(relatorio_estoque)

    # Histórico de movimentações
    historico_movimentacao = relatorio_service.historico_movimentacao()
    print(historico_movimentacao)

if __name__ == "__main__":
    main()