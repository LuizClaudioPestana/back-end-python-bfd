class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if saldo < valor:
        raise SaldoInsuficienteError('Valor maior que o saldo atual!')
    else:
        print(f'Saque realizado com sucesso. Saldo atual: {saldo - valor}')

try:
    sacar(100, 50)
    sacar(100, 101)
except SaldoInsuficienteError as e:
    print(f'Erro no saque: {e}')