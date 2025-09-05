def dividir(a, b):
    if b == 0:
        raise('O valor não pode ser divisível por zero.')
    else:
        return a / b
    
print(dividir(10, 0))