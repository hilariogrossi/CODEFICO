'''Dada uma matriz quadrada de tamanho N x N (ou seja, mesma quantidade de linhas e colunas), 
implemente as seguintes funções, analise suas complexidades pela notação O e sua classe de 
complexidade: Função 1: soma_elementos(matriz): Retorna a soma de todos os elementos da matriz.
Função 2: media_diagonal_principal(matriz): Retorna a média dos elementos da diagonal principal da
matriz. Função 3: Função matriz_transposta(matriz): Retorna a matriz transposta, ou seja, troca as
linhas pelas colunas e as colunas pelas linhas. Exemplo: Entrada:
matriz1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
Console: Soma = 45 | Media diagonal = a média da diagonal principal é 5 | A matriz transposta é =
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]'''

def soma_elementos(matriz):
    soma = 0

    for l in range(len(matriz)):
        for c in range(len(matriz)):
            soma += matriz[l][c]

    return soma


def media_diagonal_principal(matriz):
    soma = media = 0

    for l in range(len(matriz)):
        for c in range(len(matriz)):
            if l == c:
                soma += matriz[l][c]
                media = soma / len(matriz)

    return media


def matriz_transposta(matriz):
    matriz_transposta = []
    
    for l in range(len(matriz)):
        linha = []
        for c in range(len(matriz)):
            elemento = matriz[c][l]
            
            linha.append(elemento)
    
        matriz_transposta.append(linha)
    
    return matriz_transposta


matriz_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f'\nA soma dos elementos da matriz é: {soma_elementos(matriz_1)}')

print(f'\nA média da soma da diagonal principal da matriz é: {media_diagonal_principal(matriz_1)}')

print('\nMatriz transposta:')
for i in matriz_transposta(matriz_1):
    print(f'\n{i}')

print()
