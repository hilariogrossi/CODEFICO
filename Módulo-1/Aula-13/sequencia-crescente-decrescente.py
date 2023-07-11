'''Escreva um programa que leia dois números inteiros positivos, n1 e n2, e imprima uma figura tal
como a mostrada a seguir, onde n1 é o de linhas e n2 é o número de colunas da figura.
No exemplo abaixo n1 = 5 e n2 = 8.
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
Caso seja informado número inferior a zero para n1 ou n2 a seguinte mensagem deve ser impressa:
"Dados de entrada inválidos" e novos dados de entrada são solicitados. (for para impressão de
padrões em linha e colunas)'''

n1 = int(input('\nEntre com um número inteiro e positivo: '))
n2 = int(input('\nEntre com outro número inteiro e positivo: '))

while n1 < 0 or n2 < 0:
    print('\nDADOS DE ENTRADA INVÁLIDOS.\n')
    n1 = int(input('\nEntre com um número inteiro e positivo: '))
    n2 = int(input('\nEntre com outro número inteiro e positivo: '))

for i in range(1, n1 + 1):
    if i % 2 == 1:
        for j in range(1, n2 + 1):
            print(f'{j}', end=' ')
    else:
        for k in range(n2, 0, -1):
            print(f'{k}', end=' ')

    print()
