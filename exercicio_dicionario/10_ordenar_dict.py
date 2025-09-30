pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}

ordenado = sorted(pontuacoes.items(), key=lambda x: x[1], reverse=True)

for nome, pontos in ordenado:
    print(f"{nome}: {pontos}")
