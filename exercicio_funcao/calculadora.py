def calculadora(operacao, a, b):
    def somar(x, y):
        return x + y

    def subtrair(x, y):
        return x - y

    def multiplicar(x, y):
        return x * y

    def dividir(x, y):
        if y == 0:
            return "O número não pode ser dividido por zero."
        return x / y

    operacoes = {
        "somar": somar,
        "subtrair": subtrair,
        "multiplicar": multiplicar,
        "dividir": dividir
    }

    if operacao in operacoes:
        return operacoes[operacao](a, b)
    else:
        return "Operação inválida!"

print(calculadora("somar", 10, 5)) 
print(calculadora("subtrair", 10, 5))
print(calculadora("multiplicar", 10, 5))
print(calculadora("dividir", 10, 5))  
print(calculadora("dividir", 10, 0)) 
print(calculadora("potencia", 10, 5))   
