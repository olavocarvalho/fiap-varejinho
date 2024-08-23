class Recibo:
    def gerar(self, venda):
        return f"Recibo: {venda['quantidade']}x {venda['produto']} - Total: R${venda['valor_total']:.2f}"