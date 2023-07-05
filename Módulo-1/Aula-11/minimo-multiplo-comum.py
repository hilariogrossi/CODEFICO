'''Faça um programa que calcule o mínimo múltiplo comum (MMC) de dois inteiros.'''

num_1 = int(input('\nEntre com um número inteiro: '))
num_2 = int(input('\nEntre com outro número inteiro: '))

cont = num_1
parada = 0

while parada == 0:
    if cont % num_1 == 0 and cont % num_2 == 0:
        parada = 1
    else:
        cont += 1

print(f'\nO MMC de {num_1} e {num_2} é "{cont}".\n')
