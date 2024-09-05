from flask import Blueprint, request, jsonify
from application.service.estoque_service import EstoqueService
from infrastructure.repositories.estoque_repository import EstoqueRepository
import pyodbc

# Conexão ao banco de dados
connection_string = "Driver={ODBC Driver 17 for SQL Server};Server=KARINA;Database=fiapinho;Trusted_Connection=yes;"
db_conexao = pyodbc.connect(connection_string)

estoque_repo = EstoqueRepository(db_conexao)
estoque_service = EstoqueService(estoque_repo)

# Criando um blueprint para estoque
estoque_bp = Blueprint('estoque', __name__)

@estoque_bp.route('/', methods=['GET'])
def listar_produtos():
    produtos = estoque_service.selecionar_todos_produtos()
    return jsonify([vars(produto) for produto in produtos])

@estoque_bp.route('/<codigo>', methods=['PUT'])
def atualizar_produto(codigo):
    dados = request.json
    produto = estoque_service.buscar_produto(codigo)
    if produto:
        produto.quantidade = dados.get('quantidade', produto.quantidade)
        estoque_service.atualizar_produto(codigo, produto.quantidade)
        return jsonify({'message': 'Produto atualizado com sucesso!'})
    return jsonify({'message': 'Produto não encontrado!'}), 404
