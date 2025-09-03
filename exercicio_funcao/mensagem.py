def mensagem(nome):
    if nome == '':
        return('Olá, visitante.')
    else:
        return(f'Olá, {nome}')
        
print(mensagem(''))