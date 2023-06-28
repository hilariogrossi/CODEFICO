'''Faça um programa que solicite um número ao usuário e, em seguida, faça uma contagem regressiva
a partir desse número até 0. Imprima cada número no console.'''

num = float(input('Entre com o número para contagem regressiva: '))

while num >= 0:
    print(f'\n{num:5.2f}\t')
    num -= 0.1
