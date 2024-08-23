# main.py

from vestuario import Vestuario
from produto import Produto
from eletronico import Eletronico
from estoque import Estoque

def main():
    # Inicializa o estoque
    estoque = Estoque()

    # Criar produtos de vestuário
    vestuario1 = Vestuario.criar(
        nome="Camisa Polo",
        categoria="Roupas",
        quantidade=10,
        preco=80.0,
        descricao="Camisa polo de algodão",
        fornecedor="Fornecedor Roupas",
        tamanho="M",
        material="Algodão"
    )

    vestuario2 = Vestuario.criar(
        nome="Calça Jeans",
        categoria="Roupas",
        quantidade=5,
        preco=120.0,
        descricao="Calça jeans azul escura",
        fornecedor="Fornecedor Roupas",
        tamanho="42",
        material="Denim"
    )

    # Adicionar produtos ao estoque
    estoque.adicionar_produto(vestuario1)
    estoque.adicionar_produto(vestuario2)

    # Listar produtos
    print("Produtos no estoque:", estoque.listar_produtos())

    # Remover produtos do estoque
    estoque.remover_produto(vestuario2.codigo, 3)
    estoque.remover_produto(vestuario2.codigo, 2)  # Deve deletar o produto

    # Atualizar produto
    estoque.atualizar_produto(vestuario1.codigo, quantidade=2)

    # Listar produtos após atualizações
    print("Produtos no estoque após atualizações:", estoque.listar_produtos())

if __name__ == "__main__":
    main()
