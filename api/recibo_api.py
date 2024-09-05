from flask import Blueprint, jsonify
from application.service.recibo_service import ReciboService
from application.service.vendas_service import VendasService
from infrastructure.repositories.recibo_repository import ReciboRepository
import pyodbc

# Conexão ao banco de dados
connection_string = "Driver={ODBC Driver 17 for SQL Server};Server=KARINA;Database=fiapinho;Trusted_Connection=yes;"
db_conexao = pyodbc.connect(connection_string)

recibo_repo = ReciboRepository(db_conexao)
recibo_service = ReciboService(recibo_repo)

# Criando um blueprint para recibos
recibo_bp = Blueprint('recibos', __name__)

@recibo_bp.route('/<int:id_venda>', methods=['GET'])
def gerar_recibo(id_venda):
    venda = VendasService.buscar_venda(id_venda)
    if venda:
        recibo = recibo_service.gerar_recibo(
            id_venda=id_venda,
            produto=venda.nome_produto,
            quantidade=venda.quantidade,
            valor_total=venda.valor_total
        )
        return jsonify({'recibo': recibo})
    return jsonify({'message': 'Venda não encontrada!'}), 404
