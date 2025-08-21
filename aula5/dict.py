lista_alunos = {"nome": "Luiz",
                "idade": 30,
                "endereco": ["Olinda", "268", "Peixinhos"],
                "turmas": ("turma 34", "turma 35")}

for k, v in lista_alunos.items():
    print(f"{k} : {v}")

print(lista_alunos["endereco"][0])