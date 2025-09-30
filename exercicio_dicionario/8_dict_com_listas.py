alunos = {
    "Lucas": [8, 7, 9],
    "Maria": [10, 9, 8],
    "João": [6, 7, 7]
}

for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"{nome} - Média: {media:.2f}")