from pymongo import MongoClient

# Conectar ao servidor MongoDB (por padrão, o MongoDB roda na porta 27017)
client = MongoClient('localhost', 27017)

# Acessar o banco de dados 'lojadb' e a collection 'vendas'
db = client['lojadb']
vendas_collection = db['vendas']

# Consulta 3: Retornar os clientes VIPs da loja (VIP = 1), retornando apenas o campo "nome"
clientes_vips = vendas_collection.find({"vip": 1}, {"_id": 0, "nome": 1})
for cliente in clientes_vips:
    print(cliente)

