frutas = ["banana", "manga", "laranja"]
# nova_fruta = "mamao"
# frutas.append(nova_fruta)
# print(frutas)
temperos = ["coentro", "cebola"]
# frutas.insert(1, "Teste com listas")
# frutas.insert(0, 34)
# print(frutas)

# nova_lista = frutas + temperos
# #print(nova_lista)

# print(sorted(nova_lista))
# #nova_lista.sort()
# print(nova_lista)

# salada_de_frutas = []
# for fruta in frutas:
#     salada_de_frutas.append(fruta)
#     print(fruta)
#     print(salada_de_frutas)

l1 = [1, 2, 3, 3, 4]
nova = []
for r in l1:
    if r not in nova:
        nova.append(r)
print(nova)