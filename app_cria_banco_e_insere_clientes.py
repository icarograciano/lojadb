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

