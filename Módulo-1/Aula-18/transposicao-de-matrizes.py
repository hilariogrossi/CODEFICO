'''Transposição de Matriz
Escreva um programa em Python que solicite ao usuário que digite uma matriz. O programa deve
realizar a transposição dessa matriz, trocando as linhas pelas colunas e exibir a matriz
transposta na tela. O programa deve realizar as seguintes etapas:
Solicitar ao usuário que digite o número de linhas da matriz.
Solicitar ao usuário que digite o número de colunas da matriz.
Utilizar loops for aninhados para percorrer cada posição da matriz.
Para cada posição, solicitar ao usuário que digite um valor inteiro.
Armazenar os valores na matriz.
Realizar a transposição da matriz, trocando as linhas pelas colunas.
Armazenar a matriz transposta em uma nova matriz.
Exibir a matriz transposta na tela.
O programa deve fornecer ao usuário as instruções adequadas para interagir com o programa,
preencher corretamente a matriz e exibir a matriz transposta. Por favor, observe que a matriz
transposta deve ser exibida na tela, mostrando os elementos organizados em linhas e colunas.'''

linhas = int(input('\nEntre com o número de linhas da matriz: '))
colunas = int(input('\nEntre com o número de colunas da matriz: '))
matriz = []
matriz_transposta = []

for l in range(linhas):
    linha = []
    for c in range(colunas):
        elemento = int(input(f'\nEntre com as informações da matriz [{l}, {c}]: '))
        linha.append(elemento)
    matriz.append(linha)

for c in range(colunas):
    linha_transposta = []
    for l in range(linhas):
        elemento = matriz[l][c]
        linha_transposta.append(elemento)
    matriz_transposta.append(linha_transposta)

print('\n   MATRIZ TRANSPOSTA\n')

for linha in matriz_transposta:
    for elemento in linha:
        print(f'    {elemento:3d}', end=' ')
    print()

print('\n')
