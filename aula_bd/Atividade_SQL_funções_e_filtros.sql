# COUNT Mostre quantos alunos estão cadastrados na tabela Aluno. Utilize a função COUNT.
SELECT COUNT(*) AS total_alunos
FROM Aluno;

#MIN Mostre a menor mensalidade entre todos os cursos cadastrados. Utilize a função MIN.
SELECT MIN(mensalidade) AS menor_mensalidade
FROM Curso;

#MAX Mostre a maior nota1 registrada entre todos os alunos. Utilize a função MAX.
SELECT MAX(nota1) AS maior_nota1
FROM Aluno;

#SUM Calcule o valor total das mensalidades de todos os cursos. Utilize a função SUM.
SELECT SUM(mensalidade) AS soma_mensalidades
FROM Curso;

#AVG Mostre a média geral da nota2 dos alunos. Utilize a função AVG.
SELECT AVG(nota2) AS media_nota2
FROM Aluno;