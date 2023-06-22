# Criar um programa que leia o número correspondente ao mês atual e os dígitos (somente os quatro
# números) de uma placa de veículo, e através do número finalizador da placa (algarismo da casa
# das unidades) determine se o IPVA do veículo vence no mês corrente. A tabela de vencimentos
# é a seguinte:
# Finais 1 e 2: mês de janeiro (1)
# Finais 3 e 4: mês de feveiro (2)
# Finais 5 e 6: mês de março (3)
# Finais 7 e 8: mês de abril (4)
# Finais 9 e 0: mês de maio (5)

placa = int(input('Digite o número da placa para verificação: '))
mes = int(input('Entre com o mês atual: '))

temp_1 = placa / 10
temp_2 = temp_1 - int(temp_1)
unidade = round(temp_2 * 10)

if unidade == 1 or unidade == 2:
    print('O mês de vencimento do IPVA é em Janeiro!')
    if mes == 1:
        print('Estamos sim no mês corrente para pagamento!')
    else:
        print('Não estamos no mês corrente para pagamento!')
elif unidade == 3 or unidade == 4:
    print('O mês de vencimento é em Fevereiro!')
    if mes == 2:
        print('Estamos sim no mês corrente para pagamento!')
    else:
        print('Não estamos no mês corrente para pagamento!')
elif unidade == 3 or unidade == 4:
    print('O mês de vencimento é em Março!')
    if mes == 3:
        print('Estamos sim no mês corrente para pagamento!')
    else:
        print('Não estamos no mês corrente para pagamento!')
elif unidade == 5 or unidade == 6:
    print('O mês de vencimento é em Abril!')
    if mes == 4:
        print('Estamos sim no mês corrente para pagamento!')
    else:
        print('Não estamos no mês corrente para pagamento!')
elif unidade == 7 or unidade == 8:
    print('O mês de vencimento é em Maio!')
    if mes == 5:
        print('Estamos sim no mês corrente para pagamento!')
    else:
        print('Não estamos no mês corrente para pagamento!')
elif unidade == 9 or unidade == 0:
    print('O mês de vencimento é em Junho!')
    if mes == 6:
        print('Estamos sim no mês corrente para pagamento!')
    else:
        print('Não estamos no mês corrente para pagamento!')
