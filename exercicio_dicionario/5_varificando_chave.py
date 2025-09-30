def contar_palavras(lista_palavras):
    contagem = {}
    for palavra in lista_palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
resultado = contar_palavras(palavras)

print(resultado)
