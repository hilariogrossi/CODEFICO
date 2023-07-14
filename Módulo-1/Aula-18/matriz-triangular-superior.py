'''Uma matriz triangular superior é uma matriz quadrada onde todos os elementos abaixo da diagonal
principal são nulos (com valor zero). Por exemplo:
2 3 8 9
0 1 4 6
0 0 2 1
0 0 0 8
Faça um programa que leia uma matriz da entrada no formato ilustrado abaixo:
2 3 8 9; 0 1 4 6; 0 0 2 1; 0 0 0 8 | Ou seja, o separador de coluna é o espaço e o separador de
linha é o ponto e vírgula. O programa deve indicar se a matriz da entrada é uma matriz triangular
superior ou não. Caso a matriz não seja quadrada, deve ser solicitada nova entrada.
(Conceito utilizado: regra baseada no índice para acessar elementos)'''

flag = True

while flag:
    entrada = input('\nEntre com a matriz: ')
    linhas = entrada.split(';')
    matriz = []

    for l in range(len(linhas)):
        colunas = linhas[l].split()
        matriz.append([])

        for c in range(len(colunas)):
            matriz[l].append(float(colunas[c]))

    if len(matriz) == len(matriz[0]):
        flag = False
    else:
        print(f'\nA matriz NÃO é quadrada. Tente novamente...')

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if l > c and matriz[l][c] != 0:
            flag = True

if flag:
    print('\nA matriz NÃO é triangular superior.\n')
else:
    print('\nA matriz é triangular superior.\n')
