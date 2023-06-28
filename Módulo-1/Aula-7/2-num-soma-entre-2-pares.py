# Implemente um programa que peça 2 números, e calcule a soma dos pares entres esses dois número:

n1 = int(input('\nEntre com o primeiro número: '))
n2 = int(input('\nEntre com o segundo número: '))

cont = soma = 0

if n1 < n2:
    while n1 <= n2:
        pares = n1 + cont
        if pares % 2 == 0:
            soma += pares
        n1 += 1
else:
    while n2 <= n1:
        pares = n2 + cont
        if pares % 2 == 0:
            soma += pares
        n2 += 1

print(f'\nA soma dos números pares é {soma}!\n')
