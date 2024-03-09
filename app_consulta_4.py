from pymongo import MongoClient

# Conectar ao servidor MongoDB (por padrão, o MongoDB roda na porta 27017)
client = MongoClient('localhost', 27017)

# Acessar o banco de dados 'lojadb' e a collection 'vendas'
db = client['lojadb']
vendas_collection = db['vendas']

# Consulta 4: Exibir as compras efetuadas por “Marcos”
compras_marcos = vendas_collection.find_one({"nome": "Marcos"}, {"_id": 0, "compras": 1})
print(compras_marcos)
