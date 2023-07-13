'''(Adaptado de Semana 5 - parte 3) Um aluno da UFOP é responsável pelas compras mensais de
supermercado de uma quantidade determinada de repúblicas de estudantes. Para isto, ele recebe de
cada uma das repúblicas a lista de produtos que serão comprados. Escreva um programa que simula as
compras das repúblicas. O programa deve solicitar o número de repúblicas no início, e para cada
república, solicita o número de itens e a seguir o valor de cada item.
O programa deve calcular o valor da compra de cada uma das repúblicas e armazenar os valores
totais em um vetor. O valor da compra de cada república deve ser impresso ao final,
imprimindo também o valor total de todas as compras efetuadas.
(Conceito utilizado: listas - para que servem)'''

num_republica = int(
    input('\nEntre com o número de repúblicas para as compras: '))

compras_totais = []

for i in range(num_republica):
    num = int(input(f'\nEntre com a quantidade de itens para a {i + 1}ª república: '))
    soma_republica = 0

    for j in range(num):
        valor = float(input(f'\nEntre com o valor do {j + 1}° produto: '))
        soma_republica += valor

    compras_totais.append(soma_republica)

soma_total = sum(compras_totais)

for i, valor_compra in enumerate(compras_totais):
    print(f'\nValor da compra da {i + 1}ª república: R$ {valor_compra:.2f}')

print(f'\nValor da compra total: R$ {soma_total:.2f}\n')
