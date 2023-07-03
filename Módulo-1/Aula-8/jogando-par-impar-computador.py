'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador PERDER. Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
Dicas: Utilize a função da questão 4, Utilize também a função randint, ela sorteia um numero em
um intervalo definido.Considere o intervalo de 0 a 10 como na questão anterior.'''


from random import randint


def verificar_soma_par_impar(valor1, valor2):
    soma = valor1 + valor2

    if soma % 2 == 0:
        return 'P'
    else:
        return 'I'


vitorias = 0

while True:
    jogador = input('\nEscolha [P] para par e [I] para ímpar: ').upper()

    if jogador != 'P' and jogador != 'I':
        print('\nERRO! VALOR INVÁLIDO. Digite novamente...\n')
        continue

    valor_jogador = int(input('\nEntre um número de [0 - 10]: '))

    if valor_jogador < 0 or valor_jogador > 10:
        print('\nERRO! VALOR INVÁLIDO. Digite novamente...\n')
        continue

    valor_computador = randint(0, 10)

    print(f'\nO valor do computador é: {valor_computador}.\n')

    resultado = verificar_soma_par_impar(valor_jogador, valor_computador)

    if resultado == jogador:
        print('\nVOCÊ VENDEU!\n')
        vitorias += 1
    else:
        print('VOCÊ PERDEU!')
        break

print(f'\nO valor de vitórias consecutivas é: "{vitorias}"!!!\n')
