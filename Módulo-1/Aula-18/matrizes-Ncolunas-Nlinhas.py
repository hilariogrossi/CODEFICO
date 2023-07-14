'''Faça um programa que solicita ao usuário um número inteiro N e na sequência solicita o
preenchimento de uma matriz quadrada de ordem N, ou seja, de dimensões N x N (N linhas e N colunas),
com a entrada de dados sendo feita elemento a elemento, sendo todos do tipo inteiro. Ao final, a
matriz deve ser impressa de forma a se visualizar os dados da matriz em forma de linhas e colunas.
(Conceito utilizado: matrizes como listas de listas)'''

linhas = colunas = int(input('\nEntre com a dimensão da matriz: [Números inteiros] '))
matriz = []

for l in range(linhas):
    linhas_vetor = []

    for c in range(colunas):
        elemento = int(input(f'\nEntre com o valor de [{l}], [{c}]: '))
        linhas_vetor.append(elemento)

    matriz.append(linhas_vetor)

print('\nMATRIZ:\n')

for l in range(linhas):
    for c in range(colunas):
        print(f'{matriz[l][c]}', end=' ')

    print()

print('\n')
