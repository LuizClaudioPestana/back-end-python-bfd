CREATE TABLE Aluno (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    nota1 decimal(5,2) NOT NULL,
    nota2 decimal(5,2) NOT NULL,
    data_nascimento DATE NOT NULL,
    id_turma INT,
    FOREIGN KEY (id_turma) REFERENCES Turma(id)
);

CREATE TABLE Turma (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    ano INT NOT NULL
);
INSERT INTO Turma (nome, ano) VALUES ('Turma A', 2023);
INSERT INTO Turma (nome, ano) VALUES ('Turma B', 2023);
INSERT INTO Aluno (nome, nota1, nota2, data_nascimento, id_turma) VALUES ('João Silva', 8.5, 7.0, '2005-04-15', 1);
INSERT INTO Aluno (nome, nota1, nota2, data_nascimento, id_turma) VALUES ('Maria Oliveira', 9.0, 8.5, '2004-09-22', 1);
INSERT INTO Aluno (nome, nota1, nota2, data_nascimento, id_turma) VALUES ('Pedro Santos', 6.5, 7.5, '2005-12-03', 2);
INSERT INTO Aluno (nome, nota1, nota2, data_nascimento, id_turma) VALUES ('Ana Costa', 7.0, 8.0, '2004-07-19',02);