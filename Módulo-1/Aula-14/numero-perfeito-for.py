'''Escreva um programa que solicite ao usuário um número inteiro positivo e verifique se ele é um
número perfeito. Um número perfeito é aquele cuja soma de todos os seus divisores próprios
(excluindo o próprio número) é igual ao próprio número. Por exemplo, 6 é um número perfeito,
pois 1 + 2 + 3 = 6.'''

num = int(input('\nEntre com o núemro: '))
soma = 0

for i in range(1, num):
    if num % i == 0:
        soma += i

if soma == num:
    print(f'\nO número {num} é um número perfeito.\n')
else:
    print(f'\nO número {num} NÃO é um número perfeito.\n')
