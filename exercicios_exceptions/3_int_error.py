try:
    numero = int(input('Informe um número: '))
except ValueError:
    print('Informe apenas números. Digite novamente!')
else:
    print('Valor correto!')