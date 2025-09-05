class IdadeInvalidaErro(Exception):
    pass
def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaErro("A idade não pode ser negativa")
    else:
        print(f"Idade {idade} cadastrada com sucesso!")

try:
    cadastrar_idade(25)     
    cadastrar_idade(-5)
except IdadeInvalidaErro as e:
    print(f"Erro ao cadastrar: {e}")