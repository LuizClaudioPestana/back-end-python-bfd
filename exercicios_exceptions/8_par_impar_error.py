try:
    numero = int(input('Informe um número: '))
except ValueError:
    print('Valor inválido. Digite novamente!')
else:
    if numero % 2 == 0:
        print(f'Número Par = {numero}')
    else:
        print(f'Ímpar = {numero}')
finally:
    print('Programa finalizado!')