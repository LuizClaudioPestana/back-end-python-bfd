.tables
.schema Aluno
select * from Aluno;



select *
from Aluno
inner join Turma
on id_turma = Turma.id;

select *
from Aluno
right join Turma
on id_aluno = Aluno.id;