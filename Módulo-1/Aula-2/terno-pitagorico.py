# Construa um programa que leia os dois catetos e a hipotenusa e veja se eles
# representam um terno pitagórico.

a = int(input('Informe o cateto 1: '))
b = int(input('Informe o cateto 2: '))
c = int(input('Informe a hipotenusa: '))

terno = a ** 2 + b ** 2 == c ** 2

if terno is True:
    print(f'Os números {a}, {b} e {c} representam um terno pitagórico.')
else:
    print(f'Os números {a}, {b} e {c} NÃO representam um terno pitagórico.')
