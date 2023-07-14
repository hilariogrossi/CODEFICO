''' Faça um programa que leia uma matriz no seguinte formato: o separador de coluna é o espaço e o
separador de linha é o ponto e vírgula. O programa deve solicitar ao usuário um número inteiro N,
que representa o número de operações de substituição de elementos que o usuário deseja realizar na
matriz. O programa então solicita os seguintes dados, N vezes, ou seja, para realizar N operações
de  substituição: A posição da linha a ser alterada, a posição da coluna a ser alterada, o valor
que substituirá o valor existente na posição indicada. O programa deve realizar a troca de N
elementos conforme os dados de entrada, e imprimir a matriz ao final, já com os valores
substituídos. (Conceito utilizado: acessando elemento da matriz pelo índice)'''

entrada = input('\nEntre com a matriz: ')
linha = entrada.split(';')
matriz = []

for l in range(len(linha)):
    coluna = linha[l].split()
    matriz.append([])

    for c in range(len(coluna)):
        matriz[l].append(float(coluna[c]))

N = int(input('\nEntre com o número de operações de substituição de elementos: '))

for i in range(N):
    linhas = int(input(f'\n[{i + 1}ª] - Entre com a posição da linha a ser alterada: '))
    colunas = int(input(f'\n[{i + 1}ª] - Entre com a posição da coluna a ser alterada: '))
    valor = int(input(f'\n[{i + 1}ª] - Entre com o valor a ser substituido: '))

    matriz[linhas - 1][colunas - 1] = valor

print('\n')

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        print(f'{matriz[l][c]:6.1f}', end=' ')
    
    print()

print('\n')
