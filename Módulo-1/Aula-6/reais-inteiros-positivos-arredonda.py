# Faça um programa que solicita ao usuário informar inicialmente se deseja realizar cálculos com valores "reais" ou "inteiros".
# O usuário deve entrar com "real" ou "inteiro" e caso o texto digitado não seja um destes dois o programa deve ser encerrado. Caso contrário o programa
# solicita ao usuário que entre com um valor do tipo escolhido. No caso de ter escolhido trabalhar com número inteiro positivo e faça com que o
# programa imprima todos os números de 0 até o valor, inclusive. No caso de ter escolhido trabalhar com número real o programa deve usar as funções de
# arrendondamento para imprimir os valores arrendondados para cima e para baixo.

import math

tipo = input('Digite inteiro ou real para prosseguir: ').lower()

if tipo != 'inteiro' and tipo != 'real':
    print('VOCÊ NÃO DIGITOU CORRETAMENTE. Encerrando o programa...')
else:
    if tipo == 'inteiro':
        num = int(input('Informe o número para processamento: '))
        cont = 0
        while cont <= num:
            print(cont)
            cont += 1
    else:
        num = float(input('Entre com o número para processamento: '))
        print(f'O arrendondamento para baixo do número {num} é: {math.floor(num)}\nO arredondamento para cima do número {num} é: {math.ceil(num)}')        
