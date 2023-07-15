'''Escreva um programa que leia uma matriz Mat e caso ela seja uma matriz quadrada, imprima a soma
de todos os valores da diagonal principal e da diagonal secundária de Mat. Se não for uma matriz
quadrada, imprime uma mensagem para informar que a matriz não é quadrada. (Conceito utilizado:
calculando a posição no índice). Exemplo de matriz quadrada:
2 3 8 9; 0 1 4 6; 0 0 2 1; 0 0 0 8'''

entrada = input('\nEntre com os dados da matriz em questão: ')
linhas = entrada.split(';')
matriz = []

for linha in linhas:
    colunas = linha.split()
    linha_convertida = [float(coluna) for coluna in colunas]
    matriz.append(linha_convertida)

soma_diagonal_principal = soma_diagonal_secundaria = 0
n = len(matriz)

if n == len(matriz[0]):
    for i in range(n):
        soma_diagonal_principal += matriz[i][i]
        soma_diagonal_secundaria += matriz[i][n - i - 1]

    soma = soma_diagonal_principal + soma_diagonal_secundaria
    print(f'\nSoma dos elementos das duas diagonais: {soma}\n')
else:
    print('\nA matriz não é quadrada!\n')
