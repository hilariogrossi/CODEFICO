'''Escreva um programa que leia 7 números inteiros e imprima quantos são pares e quantos são
ímpares, bem como a soma de todos os números pares e a soma de todos os números ímpares. Usando for'''

pares = impares = soma_pares = soma_impares = 0

for i in range(7):
    numero = int(input(f'\nEntre com o {i + 1}° número: '))

    if numero % 2 == 0:
        pares += 1
        soma_pares += numero
    else:
        impares += 1
        soma_impares += numero

print(f'\nA quantidade de números pares é: {pares} e de números ímpares é {impares}.')
print(f'\nA soma dos números pares é: {soma_pares} e dos números ímpares é {soma_impares}.\n')
