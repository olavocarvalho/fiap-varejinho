from domain.produto import Produto

class EstoqueRepository:
    def __init__(self, db_conexao):
        self.db_conexao = db_conexao

    def salvar_produto(self, produto):
        query = """
        INSERT INTO produtos (codigo, nome, categoria, quantidade, preco, descricao, fornecedor)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query, (produto.codigo, produto.nome, produto.categoria, produto.quantidade, produto.preco, produto.descricao, produto.fornecedor))
        self.db_conexao.commit()

    def atualizar_produto(self, produto):
        query = """
        UPDATE produtos SET quantidade = ?, preco = ?, descricao = ?, fornecedor = ? WHERE codigo = ?
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query, (produto.quantidade, produto.preco, produto.descricao, produto.fornecedor, produto.codigo))
        self.db_conexao.commit()

    def buscar_produto(self, codigo):
        query = """
        SELECT nome, codigo, categoria, quantidade, preco, descricao, fornecedor FROM produtos WHERE codigo = ?
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query, (codigo,))
        produto_dados = cursor.fetchone()
        if produto_dados:
            return Produto(*produto_dados)
        return None

    def registrar_movimentacao(self, movimentacao):
        query = """
        INSERT INTO movimentacoes (tipo, produto, codigo, quantidade, descricao)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query, (movimentacao['tipo'], movimentacao['produto'], movimentacao['codigo'], movimentacao['quantidade'], movimentacao['descricao']))
        self.db_conexao.commit()

    def selecionar_todos_produtos(self):
        """
        Retorna todos os produtos cadastrados no banco de dados.

        :return: Lista de objetos do tipo Produto.
        """
        query = """
        SELECT nome, codigo, categoria, quantidade, preco, descricao, fornecedor
        FROM produtos
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query)
        produtos = cursor.fetchall()
        return [Produto(*dados_produto) for dados_produto in produtos]
    
    def buscar_movimentacoes(self):
        """
        Retorna todas as movimentações registradas no banco de dados.

        :return: Lista de movimentações (dicionários contendo informações de cada movimentação).
        """
        query = """
        SELECT tipo, produto, codigo, quantidade, descricao
        FROM movimentacoes
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query)
        movimentacoes = cursor.fetchall()
        return [{
            'tipo': m[0],
            'produto': m[1],
            'codigo': m[2],
            'quantidade': m[3],
            'descricao': m[4]
        } for m in movimentacoes]
    
    
    def buscar_movimentacoes(self):
        """
        Retorna todas as movimentações registradas no banco de dados.

        :return: Lista de movimentações (dicionários contendo informações de cada movimentação).
        """
        query = """
        SELECT tipo, produto, codigo, quantidade, descricao
        FROM movimentacoes
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query)
        movimentacoes = cursor.fetchall()
        return [{
            'tipo': m[0],
            'produto': m[1],
            'codigo': m[2],
            'quantidade': m[3],
            'descricao': m[4]
        } for m in movimentacoes]
