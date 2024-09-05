from flask import Blueprint, jsonify
from application.service.relatorio_service import RelatorioService
from infrastructure.repositories.relatorio_repository import RelatorioRepository
from application.service.estoque_service import EstoqueService
from application.service.vendas_service import VendasService
from infrastructure.repositories.estoque_repository import EstoqueRepository
from infrastructure.repositories.vendas_repository import VendasRepository
import pyodbc

# Conexão ao banco de dados
connection_string = "Driver={ODBC Driver 17 for SQL Server};Server=KARINA;Database=fiapinho;Trusted_Connection=yes;"
db_conexao = pyodbc.connect(connection_string)

# Instanciar os repositórios e serviços
estoque_repo = EstoqueRepository(db_conexao)
vendas_repo = VendasRepository(db_conexao)
relatorio_repo = RelatorioRepository(db_conexao)

estoque_service = EstoqueService(estoque_repo)
vendas_service = VendasService(vendas_repo, estoque_service)
relatorio_service = RelatorioService(vendas_service, estoque_service, relatorio_repo)

# Criando um blueprint para relatórios
relatorio_bp = Blueprint('relatorios', __name__)

@relatorio_bp.route('/vendas', methods=['GET'])
def relatorio_vendas():
    relatorio = relatorio_service.relatorio_vendas()
    return jsonify({'relatorio': relatorio})

@relatorio_bp.route('/estoque', methods=['GET'])
def relatorio_estoque():
    relatorio = relatorio_service.relatorio_estoque()
    return jsonify({'relatorio': relatorio})

@relatorio_bp.route('/movimentacoes', methods=['GET'])
def relatorio_movimentacoes():
    relatorio = relatorio_service.historico_movimentacao()
    return jsonify({'relatorio': relatorio})