''' Faça uma função, ou melhor, um procedimento, para receber uma matriz de inteiros e fazer a
sua impressão. A matriz poderá ser de qualquer dimensão, ou seja, qualquer número de linhas e de
colunas. Faça um programa principal para testar a sua função. Use outro arquivo para chamar a
função como biblioteca. (Conceito utilizado: função para impressão de matriz (como biblioteca))'''


print('\n')
def imprime_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f'{elemento:4d}', end=' ')
        print()


matriz_principal = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 20, 30]]
imprime_matriz(matriz_principal)
print('\n')
