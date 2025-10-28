import sqlite3

def criar_conexao():
    conexao = None
    try:
        conexao = sqlite3.connect("aula_bd/escola_v2.db")
        print("Conexão estabelecida com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return conexao

def fechar_conexao(conexao):
    if conexao:
        conexao.close()
        print("Conexão fechada com sucesso.")
        
def query_alunos(conexao): 
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Aluno")
        linhas = cursor.fetchall()
        for linha in linhas:
            print(linha)
            
def query_top10_medias(conexao):
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
                       SELECT nome, (nota1 + nota2) / 2.0 AS media
                       FROM Aluno
                       ORDER BY media DESC
                       LIMIT 10
                       """)
        linhas = cursor.fetchall()
        for linha in linhas:
            print(f"Aluno: {linha[0]}, Média: {linha[1]:.2f}")

def query_aluno_turma_leftjoin(conexao):
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
                       SELECT * 
                       FROM Aluno
                       LEFT JOIN Turma 
                       ON id_turma = Turma.id
                       WHERE id_turma = 2
                       """)
        linhas = cursor.fetchall()
        for linha in linhas:
            print(linha)
      
conexao = criar_conexao()
try:
    query_alunos(conexao)
    query_top10_medias(conexao)
    query_aluno_turma_leftjoin(conexao)
finally:
    fechar_conexao(conexao)