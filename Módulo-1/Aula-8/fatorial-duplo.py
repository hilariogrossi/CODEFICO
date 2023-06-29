'''
O fatorial duplo – n‼ – é definido do seguinte modo:
n‼  =   n ×(n-2)  ×(n-4)  × ⋯ ×3 ×1 , se n é ímpar, ou
        n ×(n-2)  ×(n-4)  × ⋯ ×4 ×2 , se n é par.
Por exemplo:
9!! = 9 × 7 × 5 × 3 × 1 = 945
12!! = 12 × 10 × 8 × 6 × 4 × 2 = 46080
Defina uma função dfat, que receba como parâmetro um número inteiro positivo n e retorne o
valor de n‼, tal como definido acima.
Escreva também um programa principal que leia um
número inteiro positivo e calcule o valor do fatorial duplo desse número, usando a função
dfat, previamente definida.
O programa deve testar se o valor lido é um inteiro positivo, solicitando que seja digitado
um novo valor, caso contrário.
(Conceito utilizado: função para problema de séries)
'''

def dfat(n):
    produtorio = 1

    while n > 0:
        produtorio *= n
        n -= 2
    
    return produtorio


numero = int(input('\nEntre com um número inteiro e positivo: '))

while numero <= 0:
    numero = int(input('\nENTRADA INVÁLIDA! Entre com um número inteiro e positivo: '))

resposta = dfat(numero)

print(f'\nO fatorial duplo do número {numero} é {resposta}.\n')
