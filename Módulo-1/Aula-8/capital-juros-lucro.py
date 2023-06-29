'''
Defina uma função para calcular o valor final de um investimento de capital.
A função deve ter como parâmetros o valor do capital investido (C), a taxa de
juros anual (j), o número de anos (a) durante os quais o capital permanecerá investido
e a taxa de imposto que incidirá sobre o rendimento (ir); a função deve retornar como
resultado o valor do montante final (VF) do investimento, já descontado o imposto de
renda. As fórmulas envolvidas são:
        V = C (1 + j)^a          VF = V - (V - C)*ir
Escreva um programa para ler do teclado um valor de capital a ser investido, a taxa
anual de juros, o número de anos programado para o investimento e a taxa de imposto.
O programa deverá calcular e imprimir o valor final resultante do investimento,
utilizando a função definida acima. Deverá, também, calcular e imprimir o percentual
de lucro líquido, dado pela fórmula:
	L = (VF - C)/C * 100
(Conceito utilizado: enunciado mais elaborado)
'''

def investimento(C, j, a, ir):
    V = C * (1 + j) ** a
    VF = V - (V - C) * ir

    return VF


capital = float(input('\nEntre com o valor do capital a ser investido: '))
juros_anual = float(input('\nEntre com a taxa anual de juros: '))
quantidade_anos = int(input('\nEntre com número de anos programado: '))
imposto_renda = float(input('\nEntre com o imposto sobre o lucro: '))


valor_final = investimento(capital, juros_anual, quantidade_anos, imposto_renda)

print(f'\nO valor final resultante do investimento é R$ {valor_final:.2f}.')

L = (valor_final - capital) / capital * 100

print(f'\nO percentual do lucro líquido = {L:.2f} %\n')
