'''Faça um programa que solicita ao usuário a entrada de uma matriz quadrada usando o seguinte
formato ilustrado para uma matrix quadrada de ordem 3: 1 2 3; 4 5 6; 7 8 9 Ou seja, as linhas são
separadas por ponto-e-vírgula e os elementos nas colunas são separados por espaço em branco.
O programa deve calcular e imprimir a soma dos elementos que não fazem parte da diagonal principal.
(Conceito utilizado: entrada e caminhamento na matriz)'''

entrada = input('\nEntre com uma matriz quadrada: ')
linhas = entrada.split(';')
matriz = []

for l in range(len(linhas)):
    colunas = linhas[l].split()
    matriz.append([])

    for c in range(len(colunas)):
        matriz[l].append(float(colunas[c]))

soma = 0
print('\n')

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        print(f'{matriz[l][c]}', end='  ')
        if l != c:
            soma += matriz[l][c]
    
    print()

print(f'\nSoma sem os elementos da diagonal principal: {soma}\n')
