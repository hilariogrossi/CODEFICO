'''Escreva um código que solicite ao usuario que forneça 9 números inteiros para preencher uma
matriz 3x3. Após isso, a função deve calcular a soma de cada uma das linhas dessa matriz e armazenar
o resultado em uma lista. Também deve identificar e armazenar em outra lista todos os números 
ímpares presentes na matriz. Por fim, os resultados das duas listas são exibidos na tela.'''


def calcular(matriz):
    lista_soma = []
    impares = []

    for linha_def in matriz:
        soma_linha = sum(linha_def)
        lista_soma.append(soma_linha)

        for elemento_def in linha_def:
            if elemento_def % 2 == 1:
                impares.append(elemento_def)

    return lista_soma, impares


print('\nFORNEÇA 9 NÚMEROS PARA A CONSTRUÇÃO DE UMA MATRIZ 3 X 3')
matriz_principal = []

for linha in range(3):
    linhas = []
    for coluna in range(3):
        elemento = int(input(f'\nEntre com o elemento [{linha}][{coluna}]:  '))
        linhas.append(elemento)
    matriz_principal.append(linhas)

soma_final, impares_final = calcular(matriz_principal)

print(f'\nSoma de cada linha: {soma_final}.')
print(f'\nNúmeros ímpares: {impares_final}.\n')
