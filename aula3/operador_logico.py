# print(True and False)
# print(True or False)

idade = int(input('Informe sua idade: '))
carteira = input('Tem carteira de motorista(sim/não): ')
cachaca = input('Ingeriu bebida alcoolica(sim/não): ')

if idade >= 18 and carteira == "sim" and cachaca == 'não':
    print('Pode dirigir!')
else:
    print('Não pode dirigir!')