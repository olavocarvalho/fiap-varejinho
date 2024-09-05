from  domain.recibo import Recibo

class ReciboRepository:
    def __init__(self, db_conexao):
        self.db_conexao = db_conexao

    def salvar_recibo(self, recibo):
        query = """
        INSERT INTO recibos (id_venda, produto, quantidade, valor_total)
        VALUES (?, ?, ?, ?)
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query, (recibo.id_venda, recibo.produto, recibo.quantidade, recibo.valor_total))
        self.db_conexao.commit()

    def buscar_recibo(self, id_venda):
        query = """
        SELECT id_venda, produto, quantidade, valor_total 
        FROM recibos WHERE id_venda = ?
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query, (id_venda,))
        recibo_dados = cursor.fetchone()
        if recibo_dados:
            return Recibo(*recibo_dados)
        return None

    def buscar_todos_recibos(self):
        query = """
        SELECT id_venda, produto, quantidade, valor_total 
        FROM recibos
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query)
        recibos = cursor.fetchall()
        return [Recibo(*dados_recibo) for dados_recibo in recibos]
