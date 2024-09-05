curl -X POST http://localhost:5000/vestuario -H "Content-Type: application/json" -d '{
    "nome": "Camiseta Polo",
    "codigo": "V001",
    "quantidade": 200,
    "preco": 79.90,
    "descricao": "Camiseta Polo de algodão, cor azul, tamanho M.",
    "fornecedor": "Textil Brasil"
}'