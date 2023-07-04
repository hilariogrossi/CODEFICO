'''Escreva um programa que leia uma sequência de números inteiros e imprima quantos são pares e
quantos são ímpares, bem como a soma de todos os números pares e a soma de todos os números ímpares.
O usuário poderá entrar com qualque quantidade de números. Qualquer valor positivo é válido, mas
a entrada de um valor negativo implica no término de entrada de valores pelo usuário.'''

num = int(input('\nDigite um número inteiro e positivo: [-1 Encerra o programa]: '))

pares = impares = soma_pares = soma_impares = 0

while num >= 0:
    if num % 2 == 0:
        pares += 1
        soma_pares += num
    else:
        impares += 1
        soma_impares += num
    
    num = int(input('\nDigite um número inteiro e positivo: [-1 Encerra o programa]: '))

print(f'\nA quantidade de pares = {pares} e a sua soma = {soma_pares}.')
print(f'\nA quantidade de impares = {impares} e a sua soma = {soma_impares}.\n')
