# Descrição: Escreva um programa que receba um número inteiro do usuário e calcule a soma de todos os números inteiros de 1 até o número digitado.

num = int(input('\nEntre com um número inteiro: '))

cont = soma = 0

while cont <= num:
    soma += cont
    cont += 1

print(f'\nA soma dos números até {num} é: {soma}!\n')
