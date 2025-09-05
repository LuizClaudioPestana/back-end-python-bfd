try:
    arquivo = open('teste.txt', 'r')
    conteudo = arquivo.read()
    print(conteudo)
    arquivo.close()
finally:
    print('Arquivo lido e fechado com sucesso!')