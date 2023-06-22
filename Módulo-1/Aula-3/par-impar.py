# Faça Um programa que receba um número inteiro da entrada e verifique se
# o número é par ou ímpar.

numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print(f'O número {numero} é PAR!')
else:
    print(f'O número {numero} é ÍMPAR!')
