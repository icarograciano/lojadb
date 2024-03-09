from pymongo import MongoClient

# Conectar ao servidor MongoDB (por padrão, o MongoDB roda na porta 27017)
client = MongoClient('localhost', 27017)

# Acessar o banco de dados 'lojadb' e a collection 'vendas'
db = client['lojadb']
vendas_collection = db['vendas']

# Consulta 1: Retornar todos os documentos da collection
todos_documentos = vendas_collection.find()
for documento in todos_documentos:
    print(f"Documentos: {documento}")

