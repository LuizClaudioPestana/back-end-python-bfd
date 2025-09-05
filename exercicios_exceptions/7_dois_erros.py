try:
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
    div = num1 / num2
except ZeroDivisionError:
    print('Valor não pode ser dividido por zero!')
except ValueError:
    print('Valor inválido. Digite novamente!')