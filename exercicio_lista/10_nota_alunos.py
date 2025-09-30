notas = []

for i in range(2):
    aluno_notas = []
    print(f"\nDigite as notas do aluno {i+1}:")
    for j in range(3):
        nota = float(input(f"Nota {j+1}: "))
        aluno_notas.append(nota)
    notas.append(aluno_notas)


for i, aluno_notas in enumerate(notas):
    media = sum(aluno_notas) / len(aluno_notas)
    print(f"Média do aluno {i+1}: {media:.2f}")
