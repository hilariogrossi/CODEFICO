'''Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos
 quadrados dos elementos do vetor'''

vetor_1 = vetor_2 = []
soma_quadrados = 0

for i in range(10):
    numeros = input(f'\nEntre com o {i + 1}° número: ')
    vetor_1.append(int(numeros))

    soma_quadrados += vetor_1[i] ** 2

print(f'\nA soma dos quadrados dos vetores é: {soma_quadrados}')

for j in range(vetor_1[i]):
    vetor_2.append(vetor_1[j] ** 2)

print(f'\nO quadrado dos números do vetor é: {vetor_2}\n')
