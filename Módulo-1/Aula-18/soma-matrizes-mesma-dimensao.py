'''Soma de Matrizes de Mesma Dimensão
Escreva um programa em Python que solicite ao usuário que digite duas matrizes de mesma dimensão,
ou seja, com o mesmo número de linhas e colunas. O programa deve realizar a soma das duas matrizes
e exibir o resultado na tela. O programa deve realizar as seguintes etapas:
Solicitar ao usuário que digite o número de linhas e colunas das matrizes.
Utilizar loops for aninhados para percorrer cada posição das matrizes.
Para cada posição, solicitar ao usuário que digite um valor inteiro para a primeira matriz.
Armazenar os valores da primeira matriz.
Repetir o passo 3 e 4 para preencher a segunda matriz.
Realizar a soma das duas matrizes, somando os elementos correspondentes de cada posição.
Armazenar o resultado da soma em uma nova matriz.
Exibir o resultado da soma das matrizes na tela.
O programa deve fornecer ao usuário as instruções adequadas para interagir com o programa,
preencher corretamente as matrizes e exibir o resultado da soma. Por favor, observe que o
resultado da soma das matrizes deve ser exibido na tela, mostrando os elementos organizados em
linhas e colunas.'''

linhas_1 = int(input('\nEntre com o número de linhas para a 1ª matriz: '))
coluna_1 = int(input('\nEntre com o número de colunas para a 1ª matriz: '))
linhas_2 = int(input('\nEntre com o número de linhas para a 2ª matriz: '))
colunas_2 = int(input('\nEntre com o número de colunas para a 1ª matriz: '))
matriz_1 = []
matriz_2 = []

if linhas_1 != linhas_2 or coluna_1 != colunas_2:
    print('\nAs matrizes não possuem as mesmas Dimensões. Encerrando o programa...\n')
    exit()
else:
    for l in range(linhas_1):
        linha_1 = []

        for c in range(coluna_1):
            elemento_1 = int(input(f'\nEntre com os valores para a 1ª matriz [{l}, {c}]: '))
            linha_1.append(elemento_1)

        matriz_1.append(linha_1)

    for l in range(linhas_2):
        linha_2 = []

        for c in range(colunas_2):
            elemento_2 = int(input(f'\nEntre com os valores para a 1ª matriz [{l}, {c}]: '))
            linha_2.append(elemento_2)

        matriz_2.append(linha_2)

    resultado = []

    for l in range(linhas_1):
        linha = []

        for c in range(colunas_2):
            soma = matriz_1[l][c] + matriz_2[l][c]
            linha.append(soma)

        resultado.append(linha)

    print('\nRESULTADO DA SOMA DAS MATRIZES\n')

    for linha in resultado:
        for elemento in linha:
            print(f'{elemento}', end=' ')

        print()

print('\n')
