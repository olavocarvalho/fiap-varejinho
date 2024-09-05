from domain.produto import Produto

class DescontoRepository:
    def __init__(self, db_conexao):
        self.db_conexao = db_conexao

    def atualizar_preco(self, produto):
        query = """
        UPDATE produtos SET preco = ? WHERE codigo = ?
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query, (produto.preco, produto.codigo))
        self.db_conexao.commit()

    def buscar_produto(self, codigo):
        query = """
        SELECT codigo, nome, preco FROM produtos WHERE codigo = ?
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query, (codigo,))
        produto_dados = cursor.fetchone()
        if produto_dados:
            return Produto(produto_dados[0], produto_dados[1], produto_dados[2])
        return None