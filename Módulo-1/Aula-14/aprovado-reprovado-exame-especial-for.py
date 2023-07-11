'''Codifique um programa que solicite ao usuário a entrada de um valor referente ao número
de alunos em uma turma. Para cada aluno, o programa deve solicitar a entrada do seu nome
e duas notas de avaliações, que são valores entre 0 e 10.
Para cada aluno, é calculada a média das notas e como saída o programa deve imprimir o
nome do aluno e sua situação de acordo com a classificação da tabela abaixo:
Média                 Situação
< 3                   REPROVADO
>= 6                  APROVADO
3 <= MÉDIA < 6        EXAME ESPECIAL
O programa deve ainda verificar se o nome do aluno está entre os que trancaram matrícula.
Sabe-se que os alunos "João" e "Lucas" trancaram matrícula, logo, seu programa deve comparar
o nome do estudante informado com os nomes que trancaram matrícula, e caso ele tenha trancado,
sua situação final será MAT. TRANCADA, e não alguma situação a partir de sua nota.
Faça este programa utilizando somente o for para a repetição. Aproveite o código do Exercício
2 da Lista 4.'''

numero_alunos = int(input('\nEntre com o valor referente ao número de alunos da turma: '))

for i in range(numero_alunos):
    nome_aluno = input(f'\nEntre com o primeiro nome do {i + 1}° aluno: ')

    if nome_aluno == 'João' or nome_aluno == 'Lucas':
        print(f'\nO aluno {nome_aluno} está com a MATRÍCULA TRANCADA\n')
        break

    n1 = float(input('\nEntre com a primeira nota do aluno: [0 - 10] '))

    while n1 < 0 or n1 > 10:
        n1 = float(input('\nNOTA FORA DOS PADRÕES ACEITÁVEIS. Entre com a primeira nota do aluno: '))

    n2 = float(input('\nEntre com a segunda nota do aluno:  [0 - 10] '))

    while n2 < 0 or n2 > 10:
        n2 = float(input('\nNOTA FORA DOS PADRÕES ACEITÁVEIS. Entre com a segunda nota do aluno: '))

    media = (n1 + n2) / 2

    if media < 3:
        situacao = 'REPROVADO'
    elif 3 <= media < 6:
        situacao = 'de EXAME ESPECIAL'
    else:
        situacao = 'APROVADO'

    print(f'\nO aluno {nome_aluno} está {situacao} com média {media:.2f}\n')
