def dados_pessoais(**kwargs):
    print("Dados pessoais:\n")
    for chave, valor in kwargs.items():
        print(f"{chave.capitalize()}: {valor}")

dados_pessoais(nome="Ana", idade=25, cidade="Recife", profissao="Engenheira")
