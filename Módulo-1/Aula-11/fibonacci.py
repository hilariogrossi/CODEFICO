'''A série de Fibonacci é formada pela sequência: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
Escreva um programa que gere a série de Fibonacci até o N-ésimo termo. O valor de N deve ser
informado pelo o usuário no início do programa.'''

N = int(input('\nEntre com o termo para série de Fibonacci: '))

termo_1 = termo_2 = 1
cont = 3

print(f'{termo_1}\n{termo_2}')

while cont <= N:
    proximo_numero = termo_1 + termo_2
    print(f'{proximo_numero}')
    termo_2 = termo_1
    termo_1 = proximo_numero

    cont += 1
