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
--select * from ALUNO;


-- create a table
CREATE TABLE DISCIPLINA (
    Nome_disciplina varchar(50) not null,
    Numero_disciplina varchar(6) not null,
    Creditos integer,
    Departamento varchar(5),
    PRIMARY KEY (Numero_disciplina),
    unique (Nome_disciplina)
);

-- insert some values
INSERT INTO DISCIPLINA VALUES ('Introd. à ciência da computação', 'CC1310', 4, 'CC');
INSERT INTO DISCIPLINA VALUES ('Estruturas de dados', 'CC3320', 4, 'CC');
INSERT INTO DISCIPLINA VALUES ('Matemática discreta', 'MAT2410', 3, 'MAT');
INSERT INTO DISCIPLINA VALUES ('Banco de dados', 'CC3380', 3, 'CC');

-- fetch some values
--SELECT * FROM DISCIPLINA;


-- create a table
CREATE TABLE TURMA (
    Identificacao_turma integer not null,
    Numero_disciplina char(8) NOT NULL,
    Semestre varchar(10) not null,
    Ano interger not null,
    Professor varchar(50),
    PRIMARY KEY (Identificacao_turma),
    foreign key (Numero_disciplina) references DISCIPLINA (Numero_disciplina)
);

-- insert some values
INSERT INTO TURMA VALUES (85, 'MAT2410', 'Segundo', 07, 'Kleber');
INSERT INTO TURMA VALUES (92, 'CC1310', 'Segundo', 07, 'Anderson');
INSERT INTO TURMA VALUES (102, 'CC3320', 'Primeiro', 08, 'Carlos');
INSERT INTO TURMA VALUES (112, 'MAT2410', 'Segundo', 08, 'Chang');
INSERT INTO TURMA VALUES (119, 'CC1310', 'Segundo', 08, 'Anderson');
INSERT INTO TURMA VALUES (135, 'CC3380', 'Segundo', 08, 'Santos');

-- fetch some values
--SELECT * FROM TURMA;


-- create a table
CREATE TABLE HISTORICO_ESCOLAR (
  Numero_aluno integer not null,
  Identificacao_turma integer not null,
  Nota char(1),
  primary key (Numero_aluno, Identificacao_turma),
  foreign key (Numero_aluno) references ALUNO (Numero_aluno),
  foreign key (Identificacao_turma) references TURMA (Identificacao_turma)
);

-- insert some values
INSERT INTO HISTORICO_ESCOLAR VALUES (17, 112, 'B');
INSERT INTO HISTORICO_ESCOLAR VALUES (17, 119, 'C');
INSERT INTO HISTORICO_ESCOLAR VALUES (8, 85, 'A');
INSERT INTO HISTORICO_ESCOLAR VALUES (8, 92, 'A');
INSERT INTO HISTORICO_ESCOLAR VALUES (8, 102, 'B');
INSERT INTO HISTORICO_ESCOLAR VALUES (8, 135, 'A');

-- fetch some values
--SELECT * FROM HISTORICO_ESCOLAR;


-- create a table
CREATE TABLE PRE_REQUISITO (
  Numero_disciplina  char(8) NOT NULL,
  Numero_pre_requisito char(10) not null,
  primary key (Numero_disciplina, Numero_pre_requisito)
  foreign key (Numero_disciplina) references DISCIPLINA (Numero_disciplina)
);

-- insert some values
INSERT INTO PRE_REQUISITO VALUES ('CC3380', 'CC3320');
INSERT INTO PRE_REQUISITO VALUES ('CC3380', 'MAT2410');
INSERT INTO PRE_REQUISITO VALUES ('CC3380', 'CC1310');

-- fetch some values
--SELECT * FROM PRE_REQUISITO;


select Nome from ALUNO where Tipo_aluno = 2 and Curso = 'CC';


select DISCIPLINA.Nome_disciplina from DISCIPLINA join TURMA
    ON DISCIPLINA.Numero_disciplina = TURMA.Numero_disciplina
    where TURMA.Professor = 'Kleber' and (TURMA.Ano == 07 or TURMA.Ano == 08);


select TURMA.Numero_disciplina, TURMA.Semestre, TURMA.Ano,
    count(HISTORICO_ESCOLAR.Numero_aluno) as Numero_alunos
    from TURMA
    join HISTORICO_ESCOLAR ON TURMA.Identificacao_turma = HISTORICO_ESCOLAR.Identificacao_turma 
    where TURMA.Professor = 'Kleber'
    group by TURMA.Numero_disciplina, TURMA.Semestre, TURMA.Ano;


select ALUNO.Nome as Nome_aluno, DISCIPLINA.Nome_disciplina, DISCIPLINA.Numero_disciplina, 
    DISCIPLINA.Creditos, TURMA.Semestre, TURMA.Ano, HISTORICO_ESCOLAR.Nota
    from ALUNO
    join HISTORICO_ESCOLAR on ALUNO.Numero_aluno = HISTORICO_ESCOLAR.Numero_aluno
    join TURMA ON HISTORICO_ESCOLAR.Identificacao_turma = TURMA.Identificacao_turma
    join DISCIPLINA ON TURMA.Numero_disciplina = DISCIPLINA.Numero_disciplina
    where ALUNO.Tipo_aluno = 2 and ALUNO.Curso = 'CC';


INSERT INTO ALUNO VALUES ('Alves', 25, 1, 'MAT');
SELECT * FROM ALUNO;


UPDATE ALUNO SET Tipo_aluno = 2 WHERE Nome = 'Silva';
SELECT * FROM ALUNO;


INSERT INTO DISCIPLINA VALUES ('Engenharia do Conhecimento', 'CC4390', 3, 'CC');
SELECT * FROM DISCIPLINA;


DELETE FROM ALUNO WHERE Nome = 'Silva' and Numero_aluno = 17;
SELECT * FROM ALUNO;
