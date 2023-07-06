'''Constrir uma Função para ==>
Codifique um programa que leia o nome de um aluno e duas notas de avaliações N1 e N2 (valores
entre 0 e 10). A seguir é calculada a média das notas do aluno. Como saída o programa deve imprimir
o nome do aluno e sua situação final de acordo com a classificação da tabela: Média < 3 =>
Situação: REPROVADO, Média 3 <= média < 6 => Situação: EXAME ESPECIAL e Média >= 6 => Situação:
APROVADO. o programa deve ainda verificar se o nome do aluno está entre os que trancaram matrícula.
Sabe-se que os alunos "João" e "Lucas" trancaram matrícula, logo, seu programa deve comparar o nome
do estudante informado com os nomes que trancaram a matrículas e caso ele tenha trancado sua
situação final será MATRÍCULA TRANCADA e não alguma situação a partir de sua nota.
Modifique o programa abaixo para fazer também a seguinte tarefa: imprimir a nota da seguinte
forma: se a nota do aluno for um número redondo, quer dizer, um número inteiro deve imprimir a
sua nota sem a parte decimal, ou seja, somente o número inteiro. Caso contrário a nota não sendo
um valor inteiro deve imprimir a nota com apenas uma casa decimal.'''


def turma_escolar(nome, media):
    if nome == 'João' or nome == 'Lucas':
        resposta_situacao = 'com a MATRÍCULA TRANCADA'
    else:
        if media < 3:
            resposta_situacao = 'REPROVADO'
        elif 3 <= media < 6:
            resposta_situacao = 'EXAME ESPECIAL'
        else:
            resposta_situacao = 'APROVADO'

    return resposta_situacao


numero_aluno_turma = int(input('\nDIGITE O NÚMERO DE ALUNOS NA TURMA: '))

while numero_aluno_turma > 0:
    nome_aluno = input('\nDigite o nome do aluno: ')
    n1 = float(input('\nEntre com a primeira nota do aluno: '))
    n2 = float(input('\nEntre com a segunda nota do aluno: '))

    media = (n1 + n2) / 2

    resposta =  turma_escolar(nome_aluno, media)

    print(f'\nO aluno {nome_aluno} está {resposta} com a nota {media:.1f}.\n')

    numero_aluno_turma -= 1
