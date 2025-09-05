try:
    num1 = input('Informe o primeiro número: ')
    num2 = input('Informe o segundo número: ')
    divisao = num1 / num2
except ZeroDivisionError:
    print('O segundo número tem que ser diferente de zero!')
except ValueError:
    print('Informe apenas números')
except:
    print('Entre em contato com o suporte')
else:
    print('Nenhum erro ocorreu')
finally:
    print('Finalizando o try')