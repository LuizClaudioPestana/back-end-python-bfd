lista = [45, 1, 2, 'banana', 3, 'Pêra', 'azul', 8, 'laranja']
print(id(lista))
copia_lista = lista[:]
print(copia_lista)
print(id(lista))
print(id(copia_lista))