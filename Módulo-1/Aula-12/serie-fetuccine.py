'''A série de FETUCCINE é gerada da seguinte forma: os dois primieros termos são fornecidos pelo
usuário. A partir daí os termos são gerados com a soma ou subtração dos dois termos anteriores a
partir da seguinte regra:
A(i) = A(i - 1) + A(i - 2) para i ímpar // A(i) = A(i - 1) - A(i - 2) para i par
Faça um programa que solicite ao usuário um valor N inteiro. O programa deve imprimir os N
primeiros termos da série de FETUCCINE considerando A1 = 1 e A2 = 2.'''

N = int(input('\nEntre com o número de elementos da série: '))

A1 = A2 = 1
indice = 3

print('1\n1')

while indice <= N:
    if indice % 2 == 0:
        A_novo = A1 - A2
    else:
        A_novo = A1 + A2

    print(f'{A_novo}')

    A2 = A1
    A1 = A_novo

    indice += 1
