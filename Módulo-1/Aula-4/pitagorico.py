# Em matemática nomeadamente em teoria dos números un terno pitagórico é formado por três números
# naturais a, b, e c => a2 + b2 = c2 Codifique um programa que leia 3 números naturais e verifique
# se representam un terno pitagórico.
# Os primeiros ternos pitagóricos primitivos são (3, 4, 5), (5, 12, 13), (7, 24, 25), (8, 15, 17), (9, 40, 41), (11, 60, 61), (12, 35, 37), (13, 84, 85), (16, 63, 65), (20, 21, 29)...

a = int(input('Entre com o primeiro número: '))
b = int(input('Entre com o segundo número: '))
c = int(input('Entre com o terceiro número: '))

if a ** 2 + b ** 2 == c ** 2:
    print('SIM é um terno pitagórico!')
else:
    print('NÃO é um terno pitagórico!')
