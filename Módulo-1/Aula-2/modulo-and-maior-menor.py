# Implemente um programa em linguagem Python que lê um valor (i), inteiro e
# positivo e 3 valores a, b e c. Se o valor de (i) é par então calcular e
# imprimir na tela a média aritmética de a, b e c. Caso contrário, se i > 10
# então calcular e imprimir na tela a média aritmética e ponderada de a, b e c.
# Os pesos dos valores são respectivamente 2, 3 e 4.

# Dica: A média ponderada é a média aritmetica onde os númeradores são
# multiplicados pelos seus respectivos pesos e o denominador é a soma
# dos pesos.

i = int(input('Digite um número inteiro e positivo: '))

if i < 0:
    print('NÚMERO NEGATIVO. DIGITE NOVAMENTE!')
    i = int(input())

a = int(input('Informe a: '))
b = int(input('Informe b: '))
c = int(input('Informe c: '))

MA = (a + b + c) / 3
MAP = (a * 2 + b * 3 + c * 4) / 9

if i % 2 == 0 and i <= 10:
    print(f'A média aritimétrica é: {MA:.2f}!')
elif i % 2 == 0 and i > 10:
    print(f'A média ponderada é: {MAP:.2f}!')
