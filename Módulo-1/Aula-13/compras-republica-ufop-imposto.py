'''Um aluno da UFOP é responsável pelas compras mensais de supermercado de uma quantidade
determinada de repúblicas de estudantes. Para isto ele recebe de cada uma das repúblicas a lista de
produtos que serão comprados. Escreva um programa que simula as compras das república solicita o
número de itens e a seguir o valor de cada item. O programa deve calcular o valor da compra de
cada uma das repúblicas e o valor total de todas as compras efetuadas. (for aninhado)

Modifique o programa anterior para não precisar perguntar no início o número de repúblicas. Quando
se chegar ao final o estudante operador do programa deve entrar com o número 0 ou um número negativo
para o número de itens de uma república representando que quer finalizar o programa por ter
finalizada a entrada de dados de todas as repúblicas. O programa deve ainda verificar o imposto
total gasto com as compras que é calculado sobre o valor total da compra seguindo a tabela abaixo:
Valor da compra         Imposto se até 10 itens         Imposto se mais de 10 itens:
Até R$ 250                  2 %                               2,5 %
R$ 250 e R$ 500,00          3 %                               3,5 %
Acima de R$ 500,00          4 %                               4,5 %
(for dentro de while com decisão)'''

soma_total = quantidade = 0
i = 1
itens = int(input(f'\nInforme a quantidade de itens que serão comprados para a {i}ª república: '))

while itens > 0:
    quantidade += itens
    soma_republica = 0

    for j in range(itens):
        valor = float(input(f'\nInforme o valor do {j + 1}° item: '))
        soma_republica += valor

    print(f'\nA {j + 1}ª república tem que pagar R$ {soma_republica:8.2f}')

    soma_total += soma_republica

    i += 1
    
    itens = int(input(f'\nInforme a quantidade de itens que serão comprados para a {i}ª república: '))

print(f'\nO valor total da compra: R$ {soma_total:8.2f}\n')

if soma_total < 250:
    if quantidade < 10:
        imposto = 2
    else:
        imposto = 2.5
elif quantidade <= 500:
    if itens < 10:
        imposto = 3
    else:
        imposto = 3.5
elif quantidade > 500:
    if itens < 10:
        imposto = 4
    else:
        imposto = 4.5

imposto_total = soma_total * imposto / 100

print(f'\nValor total do imposto: R$ {imposto_total:8.2f}\n')
