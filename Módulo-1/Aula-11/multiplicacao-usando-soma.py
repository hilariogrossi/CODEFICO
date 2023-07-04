'''Faça um programa que calcule a multiplicação de dois números utilizando apenas a operação de soma.'''

def calcula_multiplicacao_com_soma(n1, n2):
    soma = 0
    cont = 1

    while cont <= n1:
        cont += 1
        soma += n2

    return soma


num_1 = int(input('\nEntre com o primeiro número: '))
num_2 = int(input('\nEntre com o segundo número: '))

res = calcula_multiplicacao_com_soma(num_1, num_2)

print(f'\nA multiplicação de {num_1} por {num_2} é: {res}.\n')
