import os
from pymongo import MongoClient

# Recupera a string de conexão da variável de ambiente
MONGO_URI = os.environ.get("MINHA_STRING_DE_CONEXAO_MONGO")

# Conecta ao MongoDB
client = MongoClient(MONGO_URI)
db = client.nome_do_seu_banco_de_dados
