livros = ["1984", "O Hobbit", "Dom Casmurro"]
print(livros)

print("Primeiro:", livros[0])
print("Último:", livros[-1])

livros.append("A Revolução dos Bichos")
livros.append("Harry Potter")
print(livros)

livros.insert(1, "Duna")
print(livros)

if "Silêncio dos inocentes" in livros:
    livros.remove("Silêncio dos inocentes")
else:
    print("Livro não encontrado")
print(livros)

for livro in livros:
    print(f"O livro {livro} é interessante")
