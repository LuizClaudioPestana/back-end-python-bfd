matriz = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

print(matriz[1][2])

tridimensional = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                  [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                  [[1, 2, 3], [4, 5, 6], [1, 2, 3]]]

print(tridimensional[0][1][1])

lista = []
for i in range(10):
    lista.append(i)
print(lista)

lista2 = [i for i in range(10) if i%2 == 0]
print(lista2)
    