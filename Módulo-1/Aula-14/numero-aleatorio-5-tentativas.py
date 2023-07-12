'''Escreva um programa que solicite ao usuário que adivinhe um número entre 1 e 100. O programa
gerará um número aleatório e o usuário terá que adivinhar qual é esse número. O programa dará dicas
ao usuário indicando se o número a ser adivinhado é maior ou menor do que o número fornecido.
O usuário terá um número limitado de 5 tentativas para adivinhar o número correto. O programa
deve informar se o usuário acertou ou excedeu o número máximo de tentativas.
DICA: utilize random.randint() para gerar o numero.'''

from random import randint

numero_computador = randint(0, 100)
cont = 1

while cont <= 5:
    numero_usuario = int(input('\nEntre com número para conferência: [0 - 100] '))

    if numero_usuario == numero_computador:
        print(f'\nPARABÉNS! Você acertou em {cont} tentativas.\n')
        break
    elif numero_usuario > numero_computador:
        print(f'\nO número do computador é MENOR que {numero_usuario}!')
        print(f'\nVOCÊ ERROU. Você ainda tem {5 - cont} tentativas.')
    elif numero_usuario < numero_computador:
        print(f'\nO número do computador é MAIOR que {numero_usuario}!')
        print(f'\nVOCÊ ERROU. Você ainda tem {5 - cont} tentativas.')

    cont += 1

    if cont == 6:
        print(f'\nVocê excedeu o número máximo de tentativas. O número secreto era {numero_computador}.\n')
