from domain.recibo import Recibo

class ReciboService:
    def __init__(self, recibo_repo):
        self.recibo_repo = recibo_repo

    def gerar_recibo(self, id_venda, produto, quantidade, valor_total):
        recibo = Recibo(id_venda, produto, quantidade, valor_total)
        self.recibo_repo.salvar_recibo(recibo)
        return recibo.gerar()

    def buscar_recibo(self, id_venda):
        recibo = self.recibo_repo.buscar_recibo(id_venda)
        if recibo:
            return recibo.gerar()
        return f"Recibo da venda {id_venda} não encontrado."

    def buscar_todos_recibos(self):
        recibos = self.recibo_repo.buscar_todos_recibos()
        return [recibo.gerar() for recibo in recibos]
