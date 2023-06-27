# Escreva um programa em Python que gere um número inteiro aleatório entre 1 e 100 e desafie o
# usuário a adivinhar esse número. O programa deve fornecer dicas ao usuário, informando se o
# número que ele digitou é maior ou menor do que o número a ser adivinhado. O programa deve
# continuar executando até que o usuário acerte o número. Ao final, exiba a quantidade de 
# tentativas que o usuário fez para acertar.

from random import randint

print('\nBem-vindo ao jogo de adivinhar o número.\nTente adivinhar qual número eu estou pensando (entre 1 e 100).\n')

sorteio = randint(0, 100)

tentativa = 1
palpite = - 1

while palpite != sorteio:
    palpite = int(input('Digite o seu palpite: '))

    if sorteio < palpite:
        print(f'\nO número que estou pensando é menor do que {palpite}. Tente novamente\n')
    elif sorteio > palpite:
        print(f'\nO número que estou pensando é maior do que {palpite}. Tente novamente.\n')
    else:
        print(f'\nVocê acertou em {tentativa} tentativas!\n')
    tentativa += 1
