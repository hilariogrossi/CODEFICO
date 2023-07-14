'''Preenchimento e Exibição de Matriz:
Escreva um programa em Python que solicite ao usuário que digite as dimensões de uma matriz
(número de linhas e colunas). Em seguida, o programa deve pedir ao usuário que preencha a matriz
digitando valores inteiros para cada posição. Ao final, o programa deve exibir a matriz na tela.
O programa deve realizar as seguintes etapas:
Solicitar ao usuário que digite o número de linhas da matriz.
Solicitar ao usuário que digite o número de colunas da matriz.
Utilizar loops for aninhados para percorrer cada posição da matriz.
Para cada posição, solicitar ao usuário que digite um valor inteiro.
Armazenar os valores na matriz.
Exibir a matriz na tela.
O programa deve fornecer ao usuário as instruções adequadas para interagir com o programa,
preencher corretamente a matriz e exibir a matriz na tela.
Por favor, observe que a matriz será exibida no formato de linhas e colunas, separando os elementos
por espaço. Cada linha da matriz deve ser exibida em uma nova linha.'''

linhas = int(input('\nDigite o número de linhas da matriz: '))
colunas = int(input('\nDigite o número de colunas da matriz: '))

matriz = []

for l in range(linhas):
    linha = []

    for c in range(colunas):
        elemento = int(input(f'\nEntre com a linha {l}, coluna {c} da matriz: '))
        linha.append(elemento)

    matriz.append(linha)

print('\n   MATRIZ\n')

for l in range(linhas):
    for c in range(colunas):
        print(f'{matriz[l][c]:4d}', end=' ')

    print()

print('\n')
