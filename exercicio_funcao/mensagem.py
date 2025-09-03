def mensagem(nome):
    if nome == '':
        print('Olá, visitante.')
    else:
        return(f'Olá, {nome}')
        
print(mensagem(''))