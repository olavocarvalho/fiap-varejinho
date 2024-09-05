from infrastructure.repositories.produto_repository import ProdutoRepository
from domain.eletronicos import Eletronicos

class EletronicosRepository(ProdutoRepository):
    def __init__(self, db_conexao):
        super().__init__(db_conexao)

    # Caso você precise de um método específico para buscar apenas eletrônicos
    def buscar_todos_eletronicos(self):
        query = """
        SELECT nome, codigo, categoria, quantidade, preco, descricao, fornecedor 
        FROM produtos WHERE categoria = 'Eletrônicos'
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query)
        produtos = cursor.fetchall()
        return [Eletronicos(*dados_produto) for dados_produto in produtos]
