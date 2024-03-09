from pymongo import MongoClient

# Conectar ao servidor MongoDB (por padrão, o MongoDB roda na porta 27017)
client = MongoClient('localhost', 27017)

# Acessar o banco de dados 'lojadb' e a collection 'vendas'
db = client['lojadb']
vendas_collection = db['vendas']

# Consulta 5: Retornar todos os nomes de produtos comprados por todos os clientes
nomes_produtos = vendas_collection.distinct("compras.produto")
print(nomes_produtos)
