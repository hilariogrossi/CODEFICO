'''Gerador de número secreto e palpite por input do usuário.'''

from random import randint


def gerar_numero_secreto():
    numero_secreto = randint(1, 100)
    return numero_secreto


def verificar_palpite(palpite, numero_secreto):
    if palpite == numero_secreto:
        return 'Acertou!'

    elif palpite > numero_secreto:
        return 'Muito Alto'

    elif palpite < numero_secreto:
        return 'Muito Baixo'


def jogar():
    tentativas = 0
    numero_secreto = gerar_numero_secreto()

    while True:
        palpite = int(input('\nTente adivinhar o número secreto: [1 - 100] => '))
        resultado = verificar_palpite(palpite, numero_secreto)
        tentativas += 1

        if resultado == 'Acertou!':
            print(f'\nParabéns! Você acertou em {tentativas} tentativas.\n')
            break

        elif resultado == 'Muito Alto':
            print('\nTente um número menor...')

        elif resultado == 'Muito Baixo':
            print('\nTente um número mais alto...')

    nova_jogada = int(input('\nDeseja jogar novamente? [1] SIM [2] NÃO: '))

    if nova_jogada == 1:
        jogar()
    else:
        print('\n"Obrigado por jogar!"\n')

jogar()
