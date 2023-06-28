'''Codifique um programa que leia o nome de um aluno e duas notas de avaliações N1 e N2 (valores
entre 0 e 10). A seguir é calculada a média das notas do aluno. Como saída o programa deve imprimir
o nome do aluno e sua situação final de acordo com a classificação da tabela: Média < 3 => 
Situação: REPROVADO, Média 3 <= média < 6 => Situação: EXAME ESPECIAL e Média >= 6 => Situação:
APROVADO. o programa deve ainda verificar se o nome do aluno está entre os que trancaram matrícula.
Sabe-se que os alunos "João" e "Lucas" trancaram matrícula, logo, seu programa deve comparar o nome
do estudante informado com os nomes que trancaram a matrículas e caso ele tenha trancado sua
situação final será MATRÍCULA TRANCADA e não alguma situação a partir de sua nota.'''

nome = input('\nEntre com seu primeiro nome: ')

if nome == 'João' or nome == 'Lucas':
    print(f'\nO(A) aluno(a) {nome} está com a MATRÍCULA TRANCADA!\n')
else:
    N1 = float(input('\nEntre com a primeira nota: '))
    N2 = float(input('\nEntre com a segunda nota: '))

    media = (N1 + N2) / 2

    if media < 3:
        print(f'\nO(A) aluno(a) {nome} está REPROVADO!\n')
    elif 3 <= media < 6:
        print(f'\nO(A) aluno(a) {nome} está de EXAME ESPECIAL!\n')
    else:
        print(f'\nO(A) aluno(a) {nome} está de APROVADO!\n')
