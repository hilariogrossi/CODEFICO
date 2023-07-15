'''Escreva uma função em Python que recebe duas matrizes como entrada do usuário e retorna a matriz
resultante da multiplicação entre elas. Lembre-se que as matrizes são válidas para multiplicação, 
somente se possuirem dimensões compatíveis. Ou seja, o número de colunas da primeira matriz tem que
ser o mesmo que o numero de linhas da segunda matriz.'''

import numpy as np


def multiplicacao_matrizes():
    linhas_1 = int(input('\nEntre com o número de linhas da primeira matriz: '))
    colunas_1 = int(input('\nEntre com o número de colunas da primeira matriz: '))
    linhas_2 = int(input('\nEntre com o número de linhas da segunda matriz: '))
    colunas_2 = int(input('\nEntre com o número de colunas da segunda matriz: '))
    matriz_1 = []
    matriz_2 = []

    if colunas_1 != linhas_2:
        print('Matrizes incompatíveis')
        return

    for linha_1 in range(linhas_1):
        linha_1_1 = []
        for coluna_1 in range(colunas_1):
            elemento_1 = int(input(f'\nEntre com os elementos da matriz 1 [{linha_1}][{coluna_1}]: '))
            linha_1_1.append(elemento_1)
        matriz_1.append(linha_1_1)
    
    for linha_2 in range(linhas_2):
        linha_2_2 = []
        for coluna_2 in range(colunas_2):
            elemento_2 = int(input(f'\nEntre com os elementos da matriz 1 [{linha_2}][{coluna_2}]: '))
            linha_2_2.append(elemento_2)
        matriz_2.append(linha_2_2)

    multiplicacao = np.dot(matriz_1, matriz_2)

    return multiplicacao


print(f'\n{multiplicacao_matrizes()}\n')
