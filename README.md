# Projeto fiap varejinho

Este repositório contém o projeto de faculdade desenvolvido pelo time composto por Cristiano Dias, Márcia Rosano, Ana Martins, Olavo Carvalho e Luiz Cerqueira. O objetivo do projeto é simular o funcionamento de uma loja varejista utilizando a linguagem de programação Python, implementando diversas funcionalidades essenciais para o gerenciamento de produtos, vendas e estoque.

## Estrutura do Projeto

O projeto é dividido em diversas classes que representam diferentes aspectos da operação de uma fiap varejinho. Abaixo estão descritas as principais classes e seus respectivos métodos:

### 1. Classe: `Desconto`
- **Método: `aplicar`**
  - Aplica um desconto em um produto específico.

### 2. Classe: `Produto`
- **Métodos:**
  - `criar`: Cria um novo produto.
  - `editar`: Edita as informações de um produto existente.
  - `deletar`: Deleta um produto do sistema.
  - `selecionar`: Seleciona um produto específico.
  - `selecionar_todos`: Retorna uma lista de todos os produtos.

### 3. Classe: `Eletronicos` (herda de `Produto`)
- **Construtor:**
  - Define as propriedades específicas para produtos eletrônicos.

### 4. Classe: `Vestuario` (herda de `Produto`)
- **Construtor:**
  - Define as propriedades específicas para produtos de vestuário.

### 5. Classe: `Estoque`
- **Métodos:**
  - `adicionar`: Adiciona um novo produto ao estoque.
  - `remover`: Remove um produto do estoque.
  - `atualizar`: Atualiza as quantidades de um produto no estoque.
  - `alertar`: Gera alertas sobre produtos com baixo estoque.
  - `historico_movimentacao`: Armazena o histórico de movimentações no estoque.

### 6. Classe: `Gestor_loja`
- **Métodos:**
  - `adicionar_produto`: Adiciona um novo produto ao sistema.
  - `remover_produto`: Remove um produto do sistema.
  - `atualizar_produto`: Atualiza as informações de um produto.
  - `registrar_venda`: Registra uma nova venda.
  - `gerar_relatorio_vendas`: Gera um relatório das vendas realizadas.
  - `gerar_relatorio_estoque`: Gera um relatório detalhado do estoque.
  - `gerar_historico_movimentacao`: Gera um histórico de movimentações no estoque.
  - `verificar_alerta_estoque`: Verifica e gera alertas para produtos com estoque baixo.

### 7. Classe: `Vendas`
- **Método: `registrar`**
  - Registra uma nova venda e atualiza a movimentação no estoque.

### 8. Classe: `Recibo`
- **Método: `gerar`**
  - Gera um recibo para uma venda realizada.

### 9. Classe: `Relatorios`
- **Métodos:**
  - `relatorio_vendas`: Gera um relatório detalhado das vendas.
  - `relatorio_estoque`: Gera um relatório detalhado do estoque.
  - `historico_movimentacao`: Gera o histórico de movimentações do estoque.

## Contribuição

O desenvolvimento deste projeto é uma colaboração de todos os membros da equipe. Cada membro contribuiu para a implementação das classes e métodos descritos acima, com o objetivo de criar um sistema robusto e funcional para simular o ambiente de uma fiap varejinho.

## Execução

Para executar o projeto, é necessário ter o Python instalado na máquina. Clone este repositório e siga os passos abaixo:

1. Instale as dependências necessárias.
2. Execute o script principal para iniciar o sistema de fiap varejinho.
3. Utilize as funcionalidades disponíveis através das classes implementadas para gerenciar produtos, estoque, vendas e relatórios.

## Licença

Este projeto é destinado exclusivamente para fins educacionais e de estudo acadêmico.

---

Desenvolvido por Cristiano Dias, Márcia Rosano, Ana Martins, Olavo Carvalho e Luiz Cerqueira.
