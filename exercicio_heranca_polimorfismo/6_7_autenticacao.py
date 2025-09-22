class Autenticacao:
    def __init__(self, login):
        self.login = login
        
    def faz_login(self, email, senha):
        if email == 'teste@teste.com' and senha == 'senhateste':
            return print('Login realizado com sucesso!')
        else:
            return print('E-mail ou senha incorreto!')
            
    def status(self, email, senha):
        if email == 'teste@teste.com' and senha == 'senhateste':
            return print('Login Aprovado')
        else:
            return print('Login Negado')

class Permissao:
    def __init__(self):
        pass
    
    def verificar_permissao(self):
        print('Permissão verificada com sucesso!')
        
    def status(self, email, senha):
        if email == 'teste@teste.com' and senha == 'senhateste':
            return print('Login Aprovado')
        else:
            return print('Login Negado')
        
class Administrador(Autenticacao, Permissao):
    def __init__(self, login):
        super().__init__(login)
        

usuario = Administrador(login='Clicou em login!')
usuario.faz_login('teste@teste.com', 'senhateste')
usuario.verificar_permissao()
usuario.status('teste@teste.com', 'senhateste')
print(Administrador.__mro__)