'''faça um programa que use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5'''


def enesima(n):
    for i in range(1, n + 1):
        print(f'{i}' * i)


num = int(input('\nEntre com o número: '))

enesima(num)
