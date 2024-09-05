curl -X POST http://localhost:5000/eletronicos -H "Content-Type: application/json" -d '{
    "nome": "Smartphone XYZ",
    "codigo": "E001",
    "quantidade": 150,
    "preco": 2999.99,
    "descricao": "Smartphone de última geração com tela AMOLED de 6.5 polegadas, 128GB de armazenamento e 6GB de RAM.",
    "fornecedor": "TechCorp"
}'