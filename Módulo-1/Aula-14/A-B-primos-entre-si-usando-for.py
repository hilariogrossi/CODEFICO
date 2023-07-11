'''Escreva um programa que determine se dois valores inteiros e positivos A e B da
entrada são primos entre si. Dois números inteiros são ditos primos entre si, caso
não exista divisor comum aos dois números (com exceção de 1).
Faça este programa utilizando somente o for para a repetição.'''

print('\n***VERIFICA NÚMEROS SE SÃO PRIMOS ENTRE SI***')

A = int(input('\nEntre com um número inteiro e positivo: '))
B = int(input('\nEntre com outro número inteiro e positivo: '))

while A < 0:
    A = int(input('\nERRO! Entre com um número inteiro e positivo: '))

while B < 0:
    B = int(input('\nERRO! Entre com outro número inteiro e positivo: '))

flag = True

for i in range(2, A + 1):
    if A % i == 0 and B % i == 0:
        flag = False

if flag:
    print(f'\nOs números {A} e {B} são primos entre si.\n')
else:
    print(f'\nOs números {A} e {B} NÃO são primos entre si.\n')
