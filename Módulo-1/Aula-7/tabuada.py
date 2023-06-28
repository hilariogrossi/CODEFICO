'''Implemente um programa que solicite um número, e imprima a tabuada dele até o número 10'''

num = int(input('\nEntre com um número inteiro: '))

print(f'FAZENDO A TABUADA DO NÚMERO {num}!')

contador = 0

while contador <= num:
    print(f'\n{contador:2d} X {num} = {contador * num:3d}') 
    contador += 1
