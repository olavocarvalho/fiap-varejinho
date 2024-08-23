from produto import Produto

class Vestuario(Produto):
    def __init__(self, nome, categoria, quantidade, preco, descricao, fornecedor, tamanho, material):
        super().__init__(nome, categoria, quantidade, preco, descricao, fornecedor)
        self.tamanho = tamanho
        self.material = material

    @classmethod
    def criar(cls, nome, categoria, quantidade, preco, descricao, fornecedor, tamanho, material):
        vestuario = cls(nome, categoria, quantidade, preco, descricao, fornecedor, tamanho, material)
        cls._produtos.append(vestuario)
        return vestuario

    @classmethod
    def ler(cls, codigo):
        produto = super().ler(codigo)
        if produto and isinstance(cls._produtos[codigo - 1], Vestuario):
            return produto
        return None

    @classmethod
    def atualizar(cls, codigo, nome=None, categoria=None, quantidade=None, preco=None, descricao=None, fornecedor=None, tamanho=None, material=None):
        if super().atualizar(codigo, nome, categoria, quantidade, preco, descricao, fornecedor):
            for produto in cls._produtos:
                if produto.codigo == codigo and isinstance(produto, Vestuario):
                    if tamanho is not None:
                        produto.tamanho = tamanho
                    if material is not None:
                        produto.material = material
                    return True
        return False

    @classmethod
    def deletar(cls, codigo):
        for i, produto in enumerate(cls._produtos):
            if produto.codigo == codigo and isinstance(produto, Vestuario):
                del cls._produtos[i]
                return True
        return False

    @classmethod
    def listar(cls):
        return [vars(produto) for produto in cls._produtos if isinstance(produto, Vestuario)]
