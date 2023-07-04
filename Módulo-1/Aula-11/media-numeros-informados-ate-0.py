'''Faça um programa que calcule a média de n números informados pelo usuário até ele informar o
número 0. Por exemplo, se o usuário informar os números 9 6 2 8 0, o programa deve calcular a
média (9+ 6 + 2 + 8) / 4.'''

num = int(input('\nEntre com o número ou [DIGITE ZERO (0) PARA SAIR]: '))
soma = quantidade = 0

while num != 0:
    quantidade += 1
    soma += num

    media = soma / quantidade

    num = int(input('\nEntre com o número ou [DIGITE ZERO (0) PARA SAIR]: '))

if quantidade == 0:
    print('\nOps... Nenhum número foi informado! Saindo...\n')
else:
    print(f'\nA média é {media}\n')
