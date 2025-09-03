def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def aplicar_operacao(a, b, funcao_operacao):
    return funcao_operacao(a, b)

print(aplicar_operacao(3, 4, soma))           
print(aplicar_operacao(10, 4, subtracao))     
print(aplicar_operacao(6, 5, multiplicacao))  
print(aplicar_operacao(8, 2, divisao))        
print(aplicar_operacao(8, 0, divisao))        
