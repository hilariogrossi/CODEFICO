'''Preencha um vetor X de 10 elementos inteiros e positivos. Criar um vetor Y da seguinte forma:
Os elementos de Y com índice par receberão os respectivos elementos de X divididos por 2;
Os elementos de Y com índice ímpar receberão os respectivos elementos de X multiplicados por 3.
No final, imprima o vetor X e o vetor Y.'''

X = []
Y = []

for i in range(10):
    preenchendo_vetor_x = int(input(f'\nEntre com o {i}° dado: '))
    X.append(preenchendo_vetor_x)

    if i % 2 == 0:
        Y.append(X[i] / 2)
    else:
        Y.append(X[i] * 3)

print(f'\nO vetor X é: {X}')
print(f'\nO vetor Y é: {Y}\n')
