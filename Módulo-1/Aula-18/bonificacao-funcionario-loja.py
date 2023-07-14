'''A dona de uma loja precisa bonificar um de seus funcionários e por isso encomendou um programa
para lhe ajudar. O programa inicialmente solicita o número de funcionários N e o número de meses de
vendas que serão analisados. Os dados devem ser armazenado em uma matriz chamada Vendas, onde cada
linha representa um funcionário e cada coluna representa um mês. Seu programa dele solicitar, para 
cada um dos N funcionários, uma lista de valores que representa o volume de vendas daquele
funcionário ao longo dos meses, ou seja, se forem informados 6 meses, teríamos como exemplo de
vendas para o funcionário a seguinte lista: 21 33 30 35 29 28
Observe que as vendas de cada funcionário ao longo dos meses são informados em forma de uma lista,
onde cada elemento representa um mês. O programa deve identificar o vendedor que mais vendeu e
logo será comissionado, bem como o volume total vendido por ele.
(Conceito utilizado: linhas ou colunas representando vetores)'''

N = int(input('\nEntre com o número de funcionários: '))
M = int(input('\nEntre com o número de meses: '))
matriz = []

for l in range(N):
    vendas_1 = input(f'\nEntre com as vendas do {l + 1}° funcionário referente aos últimos {M} meses: ')
    vendas_2 = vendas_1.split()
    matriz.append([])

    for c in range(len(vendas_2)):
        matriz[l].append(float(vendas_2[c]))

resultado = []

for l in range(N):
    soma = sum(matriz[l])
    resultado.append(soma)

maior = -1

for i in range(N):
    if resultado[i] > maior:
        maior = resultado[i]
        posicao = i + 1

print(f'\nO vendedor a ser bonificado é o {posicao}° que vendeu R$ {maior:.2f}.\n')
