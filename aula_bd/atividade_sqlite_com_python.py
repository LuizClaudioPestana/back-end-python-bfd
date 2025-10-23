import sqlite3

def criar_conexao(db_file = 'escola_v2.db'):
    conexao = None
    try:
        conexao = sqlite3.connect(db_file)
        print("Conexão estabelecida com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return conexao

        
teste = criar_conexao()