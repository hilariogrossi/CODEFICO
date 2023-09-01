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
SELECT * FROM HISTORICO_ESCOLAR;
