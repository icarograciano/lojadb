from pymongo import MongoClient

# Conectar ao servidor MongoDB (por padrão, o MongoDB roda na porta 27017)
client = MongoClient('localhost', 27017)

# Acessar o banco de dados 'lojadb' e a collection 'vendas'
db = client['lojadb']
vendas_collection = db['vendas']

# Consulta 2: Localizar as informações da cliente “Maria”
informacoes_maria = vendas_collection.find_one({"nome": "Maria"})
print(informacoes_maria)

