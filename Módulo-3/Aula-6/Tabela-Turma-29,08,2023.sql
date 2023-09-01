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
SELECT * FROM TURMA;
