class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto):
        if not isinstance(produto, Vestuario):
            print("Erro: Somente produtos do tipo Vestuario podem ser adicionados.")
            return
        
        if produto.codigo in self.produtos:
            # Se o produto já estiver no estoque, atualize a quantidade
            self.produtos[produto.codigo]['quantidade'] += produto.quantidade
        else:
            # Adiciona o produto ao estoque
            self.produtos[produto.codigo] = vars(produto)
        self.alertar_estoque_baixo(produto.codigo)

    def remover_produto(self, codigo, quantidade):
        if codigo not in self.produtos:
            print("Erro: Produto não encontrado no estoque.")
            return
        
        if quantidade <= 0:
            print("Erro: A quantidade a ser removida deve ser maior que zero.")
            return

        produto = self.produtos[codigo]
        if produto['quantidade'] < quantidade:
            print("Erro: Quantidade a ser removida é maior que a quantidade disponível no estoque.")
            return
        
        produto['quantidade'] -= quantidade
        if produto['quantidade'] == 0:
            del self.produtos[codigo]
        else:
            self.produtos[codigo] = produto
        
        self.alertar_estoque_baixo(codigo)

    def atualizar_produto(self, codigo, nome=None, categoria=None, quantidade=None, preco=None, descricao=None, fornecedor=None, tamanho=None, material=None):
        if codigo not in self.produtos:
            print("Erro: Produto não encontrado no estoque.")
            return
        
        produto = self.produtos[codigo]
        if nome is not None:
            produto['nome'] = nome
        if categoria is not None:
            produto['categoria'] = categoria
        if quantidade is not None:
            produto['quantidade'] = quantidade
        if preco is not None:
            produto['preco'] = preco
        if descricao is not None:
            produto['descricao'] = descricao
        if fornecedor is not None:
            produto['fornecedor'] = fornecedor
        if tamanho is not None:
            produto['tamanho'] = tamanho
        if material is not None:
            produto['material'] = material

        self.produtos[codigo] = produto
        self.alertar_estoque_baixo(codigo)

    def alertar_estoque_baixo(self, codigo):
        if codigo in self.produtos:
            produto = self.produtos[codigo]
            if produto['quantidade'] <= 3:
                print(f"Alerta: O estoque do produto '{produto['nome']}' está baixo. Quantidade disponível: {produto['quantidade']}")

    def listar_produtos(self):
        return [vars(Vestuario(**produto)) for produto in self.produtos.values()]