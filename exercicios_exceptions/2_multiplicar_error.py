try:
    numero1 = int(input('Informe o primeiro número: '))
    numero2 = int(input('Informe o segundo número: '))
    mult = numero1 * numero2
except ValueError:
    print('Informe apenas números. Digite novamente!')
else:
    print('Valor correto!')