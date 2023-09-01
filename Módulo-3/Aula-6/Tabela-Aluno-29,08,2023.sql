-- create a table
CREATE TABLE ALUNO (
	Nome varchar(50) not null,
    Numero_aluno integer not null,
    Tipo_aluno integer not null,
    Curso char(4),
    primary key(Numero_aluno)
);

-- insert some values
insert into ALUNO values ('Silva', 17, 1, 'CC');
insert into ALUNO values ('Braga', 8, 2, 'CC');

-- fetch some values
select * from ALUNO;
