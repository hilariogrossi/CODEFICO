'''Faça um programa que execute a soma de todos os números de 1 até 10.000 menos os que são 
divisíveis por 5 ou 7 ou 13.'''

soma = 0

for num in range(1, 10000 + 1):
    if num % 5 == 0 or num % 7 == 0 or num % 13 == 0:
        continue

    soma += num

print(f'\nA soma dos números em questão é: {soma}.\n')
