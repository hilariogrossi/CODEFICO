# Faça um programa para verificar se um dado estudante foi aprovado, reprovado ou se está de exame
# especial ao final do semestre, a partir de sua nota final e de sua frequência no semestre.
# Para estar aprovado o estudante precisa ter ao menos 60 pontos e 75% de presença. Caso não seja
# aprovado o estudante precisa ter ao menos 40 pontos e 75% de presença para estar em exame
# especial. Caso contrário ele é reprovado.

nota = float(input('Entre com a nota do aluno: '))
frequencia = int(input('Entre com a frequência do aluno: '))

if nota >= 60 and frequencia >= 75:
    print('Aluno Aprovado!')
elif nota >= 40 and frequencia >= 75:
    print('Aluno em exame especial!')
else:
    print('Aluno reprovado!')
