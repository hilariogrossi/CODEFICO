'''O traço de uma matriz quadrada A, de dimensão n x n, é a soma dos elementos de sua diagonal
principal. Escreva um programa que receba uma matriz quadrada de entrada em formato semelhante ao
exemplo a seguir: A = 2.5 0.23 0; 0 3.82 4; 0 18 0. Observe que o separador de coluna é o espaço
e o separador de linha é o ponto e vírgula. O programa deve ainda:
a) imprimir a matriz;
b) criar um vetor constituído pelos elementos da diagonal principal de A e imprimir;
c) calcular o traço da matriz;
d) determinar o número de elementos fora da diagonal principal que são diferentes de 0.'''

entrada = input('Entre com a matriz A: ')
linhas = entrada.split(';')
matriz = []

for linha in linhas:
    colunas = linha.split()
    linha_convertida = [float(coluna) for coluna in colunas]
    matriz.append(linha_convertida)

print('\nMatriz A:\n')

cont = 0
vetor = []

for linha in matriz:
    for elemento in linha:
        print(f'{elemento:6.2f}', end=' ')

        if linha.index(elemento) != matriz.index(linha):
            if elemento != 0:
                cont += 1
        else:
            vetor.append(elemento)

    print('')

traco = sum(vetor)

print('\nVetor da diagonal: ', end='')

for elemento in vetor:
    print(f'{elemento:6.2f}', end=' ')

print(f'\n\nTraço(A) = {traco:.2f}')
print(f'\nElementos NÃO nulos fora da diagonal principal: {cont}\n')

'''ent = input('Entre com a matriz A: ')
linhas = ent.split(';')
mat = []

for l in range(len(linhas)):
    colunas = linhas[l].split()
    mat.append([])
    for c in range(len(colunas)):
        mat[l].append(float(colunas[c]))

print('\nMatriz A:')

cont = 0
vet = []

for l in range(len(mat)):
    for c in range(len(mat[l])):
        print(f'{mat[l][c]:6.2f}', end=' ')

        if l != c:
            if mat[l][c] != 0:
                cont += 1
        else:
            vet.append(mat[l][c])

    print('')

traco = sum(vet)

print('\nVetor da diagonal: ', end='')

for i in range(len(vet)):
    print(f'{vet[i]:6.2f}', end=' ')

print(f'\n\nTraço(A) = {traco:.2f}')
print(f'\nElementos NÃO nulos fora da diagonal principal: {cont}\n')'''

