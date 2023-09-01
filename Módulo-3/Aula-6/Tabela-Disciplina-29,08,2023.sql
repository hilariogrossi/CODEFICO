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
SELECT * FROM DISCIPLINA;
