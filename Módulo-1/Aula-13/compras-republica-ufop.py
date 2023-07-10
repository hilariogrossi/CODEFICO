'''Um aluno da UFOP é responsável pelas compras mensais de supermercado de uma quantidade
determinada de repúblicas de estudantes. Para isto ele recebe de cada uma das repúblicas a lista de
produtos que serão comprados. Escreva um programa que simula as compras das república solicita o
número de itens e a seguir o valor de cada item. O programa deve calcular o valor da compra de
cada uma das repúblicas e o valor total de todas as compras efetuadas. (for aninhado)'''

quantidade_republica = int(input('\nInforme a quantidade de repúblicas: '))
soma_total = 0

while quantidade_republica > 0:
    for i in range(quantidade_republica):
        itens = int(input(f'\nInforme a quantidade de itens que serão comprados para a {i + 1}ª república: '))
        soma_republica = 0

        for j in range(itens):
            valor = float(input(f'\nInforme o valor do {j + 1}° item: '))
            soma_republica += valor

        print(f'\nA {i + 1}ª república tem que pagar R$ {soma_republica:8.2f}')

        soma_total += soma_republica

        quantidade_republica -= 1

    print(f'\nO valor total da compra: R$ {soma_total:8.2f}\n')
