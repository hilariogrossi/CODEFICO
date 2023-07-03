'''Um professor ainda está em dúvida em como calcular as notas de seus alunos. Ele possui
basicamente duas possibilidades: calcular a nota final com base na média aritmética ou calcular
a nota final usando uma média ponderada. O critério de decisão desde professor vai levar em
consideração a participação dos alunos em suas aulas, sendo que se a participação pode ser
boa (B) ou ruim (R). Desse modo o professor vai calcular tanto a média aritmética quanto a média
ponderada usando os pesos (2, 3.5, 4.5) e dependendo da participação do aluno vai escolher a média
que maior for, beneficiando assim, o aluno participativo. Caso o aluno tenha participação ruim
a média a ser usada será necessariamente a aritmética. Codifique um programa que solicite ao
usuário o valor de 3 notas de um aluno, bem como uma letra que representará sua participação
B ou R. O programa então chama uma função passando as três notas e a letra referente ao
comportamento. Esta função deve retornar a nota do aluno e também a palavra "PONDERADA" caso
tenha sido usada a média ponderada ou a palavra "ARITMÉTICA" casa tenha sido usada a média
aritmética. Em seguida o programa principal imprime qual a nota do aluno dizendo se o mesmo
efoi aprovado ou não (nota >= 6 para aprovação) e qual o tipo de média foi usado para o
cálculo de sua nota.'''


def calculaNota(n1, n2, n3, participacao):
    aritmetica = (n1 + n2 + n3) / 3
    ponderada = n1 * 0.2 + n2 * 0.35 + n3 * 0.45

    if participacao == 'B' and ponderada > aritmetica:
        return ponderada, 'PONDERADA'
    else:
        return aritmetica, 'ARITMÉTICA'


nota_1 = float(input('\nEntre com a primeira nota do aluno: '))
nota_2 = float(input('\nEntre com a segunda nota do aluno: '))
nota_3 = float(input('\nEntre com a terceira nota do aluno: '))

participacao = input('\nEntre com [B] boa e [R] ruim para a participação do aluno: ').upper()

while participacao != 'B' and participacao != 'R':
      participacao = input('\nERRO! Entre com [B] boa e [R] ruim: ').upper()

media, metodo = calculaNota(nota_1, nota_2, nota_3, participacao)

print(f'\nNota final do aluno = {media:.2f}!')

if media >= 6:
        print(f'\nO aluno foi aprovado!\n')
else:
        print(f'\nO aluno foi reprovado!\n')

print(f'\nSUA NOTA FOI CALCULADA USANDO A MÉDIA {metodo}!\n')
