from infrastructure.repositories.produto_repository import ProdutoRepository
from domain.vestuario import Vestuario

class VestuarioRepository(ProdutoRepository):
    def __init__(self, db_conexao):
        super().__init__(db_conexao)

    # Método para buscar todos os produtos da categoria "Vestuário"
    def buscar_todos_vestuario(self):
        query = """
        SELECT nome, codigo, categoria, quantidade, preco, descricao, fornecedor 
        FROM produtos WHERE categoria = 'Vestuário'
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query)
        produtos = cursor.fetchall()
        return [Vestuario(*dados_produto) for dados_produto in produtos]