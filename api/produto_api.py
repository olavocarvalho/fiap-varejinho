from flask import Blueprint, request, jsonify
from application.service.estoque_service import EstoqueService
from domain.produto import Produto
from infrastructure.repositories.estoque_repository import EstoqueRepository
import pyodbc

# Conexão ao banco de dados
connection_string = "Driver={ODBC Driver 17 for SQL Server};Server=KARINA;Database=fiapinho;Trusted_Connection=yes;"
db_conexao = pyodbc.connect(connection_string)

estoque_repo = EstoqueRepository(db_conexao)
estoque_service = EstoqueService(estoque_repo)

# Criando um blueprint para produtos
produto_bp = Blueprint('produtos', __name__)

@produto_bp.route('/', methods=['POST'])
def adicionar_produto():
    dados = request.json
    produto = Produto(
        nome=dados['nome'],
        codigo=dados['codigo'],
        categoria=dados['categoria'],
        quantidade=dados['quantidade'],
        preco=dados['preco'],
        descricao=dados['descricao'],
        fornecedor=dados['fornecedor']
    )
    estoque_service.adicionar_produto(produto)
    return jsonify({'message': 'Produto adicionado com sucesso!'})
