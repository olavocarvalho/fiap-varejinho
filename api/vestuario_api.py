from flask import Blueprint, request, jsonify
from application.service.estoque_service import EstoqueService
from domain.vestuario import Vestuario
from infrastructure.repositories.estoque_repository import EstoqueRepository
import pyodbc

# Conexão ao banco de dados SQL Server
connection_string = "Driver={ODBC Driver 17 for SQL Server};Server=KARINA;Database=fiapinho;Trusted_Connection=yes;"
db_conexao = pyodbc.connect(connection_string)

estoque_repo = EstoqueRepository(db_conexao)
estoque_service = EstoqueService(estoque_repo)

# Criando um blueprint para vestuário
vestuario_bp = Blueprint('vestuario', __name__)

@vestuario_bp.route('/', methods=['POST'])
def adicionar_vestuario():
    dados = request.json
    vestuario = Vestuario(
        nome=dados['nome'],
        codigo=dados['codigo'],
        quantidade=dados['quantidade'],
        preco=dados['preco'],
        descricao=dados['descricao'],
        fornecedor=dados['fornecedor']
    )
    estoque_service.adicionar_produto(vestuario)
    return jsonify({'message': 'Vestuário adicionado com sucesso!'})
