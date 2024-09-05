from domain.relatorios import Relatorio

class RelatorioRepository:
    def __init__(self, db_conexao):
        self.db_conexao = db_conexao

    def salvar_relatorio(self, relatorio):
        query = """
        INSERT INTO relatorios (tipo, conteudo)
        VALUES (?, ?)
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query, (relatorio.tipo, relatorio.conteudo))
        self.db_conexao.commit()

    def buscar_relatorio(self, tipo):
        query = """
        SELECT tipo, conteudo FROM relatorios WHERE tipo = ?
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query, (tipo,))
        relatorio_dados = cursor.fetchone()
        if relatorio_dados:
            return Relatorio(*relatorio_dados)
        return None