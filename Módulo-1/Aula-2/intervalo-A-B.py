# Codifique um programa que leia os extremos de um intervalo fechado de números reais, [A; B]. A seguir o programa lê um número real qualquer e determina se o número pertence ou não ao intervalo.

inferior = float(input('Digite o limite inferior: '))
superior = float(input('Digite o limite superior: '))

numero = float(input('Digite um número qualquer: '))

if numero >= inferior and numero <= superior:
    print(f'O número {numero} PERTENCE ao intervalo.')
else:
    print(f'O número {numero} NÃO PERTENCE ao intervalo.')
