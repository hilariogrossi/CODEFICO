'''Um cromossomo com n genes pode ser representado por um vetor de n posições.
Considerando os genes 0 e 1, e dois cromossomos de tamanho n = 16 temos:
C1 = [  1  0  1  0  1  0  1  0  1  0  1  0  1  0  1  0  ]
C2 = [  1  1  1  1  1  1  1  1  0  0  0  0  0  0  0  0  ]
Definimos cruzamento de C1 e C2 através da combinação de seus genes da seguinte maneira:
1)  Escolher uma posição válida k, 0 ≤ k ≤ n-1 para indicar o ponto de corte;
2)  Copiar os elementos do vetor C1, posições de 0 até k-1, para um vetor C3;
3)  Copiar os elementos do vetor C2, posições de k até n-1, para o mesmo vetor C3.
4)  O vetor C3 é o vetor resultante do cruzamento dos vetores C1 e C2.
Desta forma, o cruzamento de C1 e C2, com ponto de corte k = 7, resultaria em:
C3 = [  1  0  1  0  1  0  1  0  0  0  0  0  0  0  0  0  ]
Escreva um programa para ler dois vetores C1 e C2, ler o valor de corte k e efetuar
o cruzamento desses vetores. Considere que o valor de k será válido.
(Conceito utilizado: combinando valores de duas listas em uma terceira)'''

C1 = input('\nEntre com a sequência do C1 (somente números): ').split()
C2 = input('\nEntre com a sequência do C2 (somente números): ').split()
C3 = []

k = int(input('\nEntre com o valor de "k": '))

for i in range(len(C1)):
    if i <= k:
        C3.append(int(C1[i]))
    else:
        C3.append(int(C2[i]))

print(f'\nC3: {C3}\n')
