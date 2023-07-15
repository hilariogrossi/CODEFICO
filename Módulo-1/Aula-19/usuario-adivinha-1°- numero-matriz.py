'''Escreva um programa em Python que solicite ao usuário que digite as dimensões de uma matriz.
Em seguida o programa deve preencher a matriz com números inteiros aleatórios de 1 a 32 e exibir
a matriz na tela sem o primeiro elemento para que o usuário adivinhe qual é esse elemento.'''

from random import randint

print('\nDIGITE AS DIMENSÕES DE UMA MATRIZ:')

linhas = int(input('\nDigite a quantidade de linhas da matriz: '))
colunas = int(input('\nDigite a quantidade de colunas da matriz: '))
matriz = []

for linha in range(linhas):
    linha = []
    for coluna in range(colunas):
        linha.append(randint(1, 32))
    matriz.append(linha)

numero_secreto = matriz[0][0]
matriz[0][0] = '?'

for linha in matriz:
    for elemento in linha:
        print(f'{elemento}', end='  ')
    print()

adivinhe = int(input('\nAdivinhe o número secreto (?): '))

if numero_secreto == adivinhe:
    print(f'\nVocê acertou o número secreto que era {numero_secreto}.\n')
else:
    print(f'\nVocê errou o número secreto que era {numero_secreto}.\n')
