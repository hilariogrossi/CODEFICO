'''Escreva um programa que leia 7 números inteiros e imprima quantos são pares e quantos são
ímpares, bem como a soma de todos os números pares e a soma de todos os números ímpares.'''

cont = 1
soma_pares = soma_impares = pares = impares = 0

while cont <= 7:
    num = int(input(f'\nEntre com o {cont}° número inteiro: '))

    if num % 2 == 0:
        pares += 1
        soma_pares += num
    else:
        impares += 1
        soma_impares += num

    cont += 1

print(f'\nA qunatidade de pares = {pares} e sua soma é {soma_pares}.')
print(f'\nA qunatidade de impares = {impares} e sua soma é {soma_impares}.\n')
