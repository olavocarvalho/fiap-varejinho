from domain.vendas import Venda

class VendasRepository:
    def __init__(self, db_conexao):
        self.db_conexao = db_conexao

    def registrar_venda(self, venda):
        query = """
        INSERT INTO vendas (codigo_produto, nome_produto, quantidade, valor_total)
        VALUES (?, ?, ?, ?)
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query, (venda.codigo_produto, venda.nome_produto, venda.quantidade, venda.valor_total))
        self.db_conexao.commit()

    def buscar_venda(self, codigo_produto):
        query = """
        SELECT codigo_produto, nome_produto, quantidade, valor_total
        FROM vendas WHERE codigo_produto = ?
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query, (codigo_produto,))
        venda_dados = cursor.fetchone()
        if venda_dados:
            return Venda(*venda_dados)
        return None

    def buscar_todas_vendas(self):
        query = """
        SELECT codigo_produto, nome_produto, quantidade, valor_total
        FROM vendas
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query)
        vendas = cursor.fetchall()
        return [Venda(*dados_venda) for dados_venda in vendas]
