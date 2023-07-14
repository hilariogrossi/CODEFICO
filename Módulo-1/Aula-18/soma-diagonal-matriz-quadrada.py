'''Soma da Diagonal Principal de uma Matriz Quadrada
Escreva um programa em Python que solicite ao usuário que digite uma matriz quadrada, ou seja,
uma matriz com o mesmo número de linhas e colunas. O programa deve calcular a soma de todos os
elementos da diagonal principal, que é a diagonal que vai do canto superior esquerdo ao canto
inferior direito. Por fim, o programa deve exibir o resultado da soma na tela. O programa deve 
realizar as seguintes etapas:
Solicitar ao usuário que digite a ordem da matriz quadrada (número de linhas e colunas são iguais).
Utilizar loops for aninhados para percorrer cada posição da matriz. Para cada posição, solicitar ao
usuário que digite um valor inteiro. Armazenar os valores na matriz. Calcular a soma dos elementos
da diagonal principal, somando os elementos nas posições [0][0], [1][1], [2][2], e assim por diante.
Exibir o resultado da soma na tela. O programa deve fornecer ao usuário as instruções adequadas
para interagir com o programa, preencher corretamente a matriz quadrada e exibir o resultado da
soma da diagonal principal. Por favor, observe que o resultado da soma dos elementos da diagonal
principal deve ser exibido na tela.'''

linhas = colunas = int(input('\nEntre com o valor da matriz quadrada: '))
matriz = []

for l in range(linhas):
    linha = []

    for c in range(colunas):
        elemento = int(input(f'\nPreencha a matriz na posição [linha {l} e coluna {c}]: '))
        linha.append(elemento)

    matriz.append(linha)

print()

soma = 0

for i in range(linhas):
    soma += matriz[i][i]

print(f'\nA soma dos elementos da diagonal principal é: {soma}\n')
