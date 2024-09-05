from flask import Blueprint, request, jsonify
from application.service.vendas_service import VendasService
from application.service.estoque_service import EstoqueService
from infrastructure.repositories.vendas_repository import VendasRepository
from infrastructure.repositories.estoque_repository import EstoqueRepository
import pyodbc

# Conexão ao banco de dados SQL Server
connection_string = "Driver={ODBC Driver 17 for SQL Server};Server=KARINA;Database=fiapinho;Trusted_Connection=yes;"
db_conexao = pyodbc.connect(connection_string)

# Instanciar os repositórios e serviços
estoque_repo = EstoqueRepository(db_conexao)
vendas_repo = VendasRepository(db_conexao)
estoque_service = EstoqueService(estoque_repo)
vendas_service = VendasService(vendas_repo, estoque_service)

# Criando um blueprint para vendas
vendas_bp = Blueprint('vendas', __name__)

@vendas_bp.route('/', methods=['POST'])
def registrar_venda():
    dados = request.json
    codigo = dados['codigo']
    quantidade = dados['quantidade']
    resultado = vendas_service.registrar_venda(codigo, quantidade)
    return jsonify({'message': resultado})

@vendas_bp.route('/', methods=['GET'])
def listar_vendas():
    vendas = vendas_service.buscar_todas_vendas()
    return jsonify(vendas)