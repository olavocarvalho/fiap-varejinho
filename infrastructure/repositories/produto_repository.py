from domain.produto import Produto

class ProdutoRepository:
    def __init__(self, db_conexao):
        self.db_conexao = db_conexao

    def criar(self, produto):
        query = """
        INSERT INTO produtos (nome, codigo, categoria, quantidade, preco, descricao, fornecedor)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query, (produto.nome, produto.codigo, produto.categoria, produto.quantidade, produto.preco, produto.descricao, produto.fornecedor))
        self.db_conexao.commit()

    def editar(self, produto):
        query = """
        UPDATE produtos 
        SET nome = ?, categoria = ?, quantidade = ?, preco = ?, descricao = ?, fornecedor = ?
        WHERE codigo = ?
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query, (produto.nome, produto.categoria, produto.quantidade, produto.preco, produto.descricao, produto.fornecedor, produto.codigo))
        self.db_conexao.commit()

    def deletar(self, codigo):
        query = """
        DELETE FROM produtos WHERE codigo = ?
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query, (codigo,))
        self.db_conexao.commit()

    def selecionar(self, codigo):
        query = """
        SELECT nome, codigo, categoria, quantidade, preco, descricao, fornecedor
        FROM produtos
        WHERE codigo = ?
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query, (codigo,))
        dados_produto = cursor.fetchone()
        if dados_produto:
            return Produto(*dados_produto)
        return None

    def selecionar_todos(self):
        query = """
        SELECT nome, codigo, categoria, quantidade, preco, descricao, fornecedor 
        FROM produtos
        """
        cursor = self.db_conexao.cursor()
        cursor.execute(query)
        produtos = cursor.fetchall()
        return [Produto(*dados_produtos) for dados_produtos in produtos]
