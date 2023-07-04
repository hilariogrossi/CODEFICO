'''Escreva um programa que recebe um número N como entrada e verifica se este número é primo. É
necessário validar se o número é inteiro e positivo e caso não seja solicitar nova valor
repetidademente. While com flag'''

num = int(input('\nDigite um número inteiro e positivo: '))

while num <= 0:
    num = int(input('\nERRO! Digite um número inteiro e positivo: '))

if num == 1:
    print('\nO número 1 NÃO é primo.\n')
    exit()

cont = 2
flag = True

while cont <= num / 2:
    if num % cont == 0:
        flag = False

    cont += 1

if flag:
    print(f'\nO número {num} é PRIMO.\n')
else:
    print(f'\nO número {num} NÃO é primo.\n')
