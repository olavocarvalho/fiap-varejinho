CREATE DATABASE fiapinho

USE fiapinho

-- Criação da tabela de Produtos
CREATE TABLE produtos (
    codigo VARCHAR(50) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    descricao VARCHAR(255),
    fornecedor VARCHAR(100)
);

-- Criação da tabela de Vendas
CREATE TABLE vendas (
    id INT IDENTITY PRIMARY KEY,
    codigo_produto VARCHAR(50),
    nome_produto VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL,
    valor_total DECIMAL(10, 2) NOT NULL,
    data_venda DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (codigo_produto) REFERENCES produtos(codigo) ON DELETE CASCADE
);

-- Criação da tabela de Movimentações de Estoque
CREATE TABLE movimentacoes (
    id INT IDENTITY PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    produto VARCHAR(100) NOT NULL,
    codigo_produto VARCHAR(50),
    quantidade INT NOT NULL,
    descricao VARCHAR(255),
    data_movimentacao DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (codigo_produto) REFERENCES produtos(codigo) ON DELETE CASCADE
);

-- Criação da tabela de Recibos
CREATE TABLE recibos (
    id INT IDENTITY PRIMARY KEY,
    id_venda INT,
    produto VARCHAR(100),
    quantidade INT NOT NULL,
    valor_total DECIMAL(10, 2) NOT NULL,
    data_recibo DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (id_venda) REFERENCES vendas(id) ON DELETE CASCADE
);

-- Criação da tabela de Relatórios
CREATE TABLE relatorios (
    id INT IDENTITY PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    conteudo TEXT,
    data_geracao DATETIME DEFAULT GETDATE()
);