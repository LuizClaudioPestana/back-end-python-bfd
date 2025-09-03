def media(*args):
    soma_total = 0
    contador = 0
    for num in args:
        soma_total = soma_total + num
        contador = num + 1
        m = soma_total / contador
        print(contador)
        return m

print(media(3, 5, 7))