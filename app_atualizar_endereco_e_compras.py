from pymongo import MongoClient

# Conectar ao servidor MongoDB (por padrão, o MongoDB roda na porta 27017)
client = MongoClient('localhost', 27017)

# Criar ou acessar o banco de dados 'lojadb'
db = client['lojadb']

# Criar ou acessar a collection 'vendas'
vendas_collection = db['vendas']

# Etapa 1: Inserir dados básicos dos clientes
clientes_data = [
    {"nome": "João", "vip": 1, "email": "joao@email.com", "telefone": ["9999-1111", "8888-1111"]},
    {"nome": "Marcos", "vip": 0, "telefone": ["9999-2222"]},
    {"nome": "Maria", "vip": 1, "email": "maria@email.com", "telefone": ["9999-3333", "8888-3333", "9988-3000"]}
]

# Inserir documentos na collection
vendas_collection.insert_many(clientes_data)

# Etapa 2: Atualizar documentos com endereços e dados de compras
endereco_data = [
    {"nome": "João", "endereco": {"rua": "Rua Um", "numero": 1000, "complemento": "Apto 1 Bloco 1", "cidade": "São Paulo", "estado": "SP"}},
    {"nome": "Marcos", "endereco": {"rua": "Rua Dois", "numero": 4000, "cidade": "Campinas", "estado": "SP"}},
    {"nome": "Maria", "endereco": {"rua": "Rua Três", "numero": 3000, "cidade": "Londrina", "estado": "PR"}}
]

compras_data = [
    {"nome": "João", "compras": [{"produto": "notebook", "preco": 5000.00, "quantidade": 1}]},
    {"nome": "Marcos", "compras": [{"produto": "Caderno", "preco": 20.00, "quantidade": 1},
                                   {"produto": "Caneta", "preco": 3.00, "quantidade": 5},
                                   {"produto": "Borracha", "preco": 2.00, "quantidade": 2}]},
    {"nome": "Maria", "compras": [{"produto": "Tablet", "preco": 2500.00, "quantidade": 1},
                                   {"produto": "Capa para tablet", "preco": 50.00, "quantidade": 1}]}
]

# Atualizar documentos na collection
for endereco in endereco_data:
    vendas_collection.update_one({"nome": endereco["nome"]}, {"$set": {"endereco": endereco["endereco"]}})

for compras in compras_data:
    vendas_collection.update_one({"nome": compras["nome"]}, {"$set": {"compras": compras["compras"]}})
