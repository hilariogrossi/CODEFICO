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
SELECT * FROM PRE_REQUISITO;
