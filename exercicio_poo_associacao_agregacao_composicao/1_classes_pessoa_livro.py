class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        self.livros_lidos = [] 

    def adicionar_livro_lido(self, livro: 'Livro'):
        if livro not in self.livros_lidos:
            self.livros_lidos.append(livro)
            print(f"{self.nome} adicionou {livro.titulo} à sua lista.")
        else:
            print(f"{self.nome} já leu {livro.titulo}.")

    def mostrar_livros_lidos(self):
        if self.livros_lidos:
            print(f"\nLivros lidos por {self.nome}:")
            for livro in self.livros_lidos:
                print(f"- {livro.titulo} por {livro.autor}")
        else:
            print(f"\n{self.nome} ainda não leu nenhum livro.")

class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

pessoa1 = Pessoa("Maria", 25)
livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Admirável Mundo Novo", "Aldous Huxley")

pessoa1.adicionar_livro_lido(livro1)
pessoa1.adicionar_livro_lido(livro2)

pessoa1.adicionar_livro_lido(livro1)

pessoa1.mostrar_livros_lidos()
