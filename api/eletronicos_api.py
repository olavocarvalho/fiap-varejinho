from flask import Blueprint, request, jsonify
from application.service.estoque_service import EstoqueService
from domain.eletronicos import Eletronicos
from infrastructure.repositories.estoque_repository import EstoqueRepository
import pyodbc

# Conexão ao banco de dados SQL Server
connection_string = "Driver={ODBC Driver 17 for SQL Server};Server=KARINA;Database=fiapinho;Trusted_Connection=yes;"
db_conexao = pyodbc.connect(connection_string)

estoque_repo = EstoqueRepository(db_conexao)
estoque_service = EstoqueService(estoque_repo)

# Criando um blueprint para eletronicos
eletronicos_bp = Blueprint('eletronicos', __name__)

@eletronicos_bp.route('/', methods=['POST'])
def adicionar_eletronico():
    dados = request.json
    eletronico = Eletronicos(
        nome=dados['nome'],
        codigo=dados['codigo'],
        quantidade=dados['quantidade'],
        preco=dados['preco'],
        descricao=dados['descricao'],
        fornecedor=dados['fornecedor']
    )
    estoque_service.adicionar_produto(eletronico)
    return jsonify({'message': 'Eletrônico adicionado com sucesso!'})
