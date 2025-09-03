def media(*args):
    soma_total = 0
    contador = 0
    for num in args:
        soma_total = soma_total + num
        contador = contador + 1
    return soma_total / contador

print(media(3, 5, 7))