'''Verificação de Matriz Diagonal
Escreva um programa em Python que solicite ao usuário que digite uma matriz. O programa deve
verificar se a matriz é uma matriz diagonal, ou seja, se todos os elementos fora da diagonal
principal são iguais a zero. Ao final, o programa deve exibir na tela se a matriz é diagonal ou não.
O programa deve realizar as seguintes etapas:
Solicitar ao usuário que digite o número de linhas da matriz.
Solicitar ao usuário que digite o número de colunas da matriz.
Utilizar loops for aninhados para percorrer cada posição da matriz.
Para cada posição, solicitar ao usuário que digite um valor inteiro.
Armazenar os valores na matriz.
Verificar se a matriz é diagonal, percorrendo todas as posições e verificando se os elementos fora
da diagonal principal são iguais a zero. Exibir na tela se a matriz é diagonal ou não. O programa
deve fornecer ao usuário as instruções adequadas para interagir com o programa, preencher
corretamente a matriz e exibir o resultado se a matriz é diagonal ou não. Por favor, observe que
o resultado da verificação se a matriz é diagonal ou não deve ser exibido na tela.'''

linhas = int(input('\nEntre com o valor da linha da matriz: '))
colunas = int(input('\nEntre com o valor da colunas da matriz: '))
matriz = []

for l in range(linhas):
    linha = []

    for c in range(colunas):
        elemento = int(input(f'\nEntre com os valores da matriz na posição [{l}, {c}]: '))
        linha.append(elemento)

    matriz.append(linha)

is_diagonal = True

for l in range(linhas):
    for c in range(colunas):
        if l != c and matriz[l][c] != 0:
            is_diagonal = False
            break

if is_diagonal:
    print('\nA matriz é diagonal.\n')
else:
    print('\nA matriz NÃO é diagonal.\n')
