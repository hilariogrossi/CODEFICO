'''Escreva um programa que determine se dois valores inteiros e positivos A e B da entrada são primos entre si.
Dois números inteiros são ditos primos entre si, caso não exista divisor comum aos dois números
(com exceção de 1)'''

A = int(input('\nEntre com o primeiro número: '))
B = int(input('\nEntre com o segundo número: '))

while A <= 0 or B <= 0:
    A = int(input('\nEntre com o primeiro número: '))
    B = int(input('\nEntre com o segundo número: '))

cont = 2
flag = True

while cont <= A / 2:
    if A % cont == 0 and B % cont == 0:
        flag = False

    cont += 1

if flag:
    print(f'\nOs números {A} e {B} são primos entre si.\n')
else:
    print(f'\nOs números {A} e {B} NÃO são primos entre si.\n')
