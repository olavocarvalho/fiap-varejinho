curl -X PUT http://localhost:5000/estoque/E001 -H "Content-Type: application/json" -d '{
    "quantidade": 120,
    "preco": 1399.99,
    "descricao": "Smartphone com tela de 6.5 polegadas e 128GB - Atualizado",
    "fornecedor": "TechCorp"
}'