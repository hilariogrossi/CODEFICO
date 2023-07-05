'''Faça um programa que desenha um retângulo de altura "a" e largura "l" usando asteriscos.
O usuário deve informar os valores de "a" e "l", que devem ser maiores que zero e tais que l > a.
Note que o seu programa deve garantir que os valores digitados sejam válidos, forçando entradas 
válidas. O programa também deve perguntar se o usuário gostaria de gerar um retângulo antes de
fazer cada impressão. O programa termina assim que o usuário responder "n" à pergunta.'''

pergunta = input('\nDeseja gerar um retângulo? [S] Sim ou [N] Não: ').upper()

while pergunta == 'S':
    a = float(input('\nEntre com a altura do retângulo: '))
    l = float(input('\nEntre com a largura do retângulo: '))

    while a <= 0 or l <= 0 or l <= a:
        print('\nDADOS INVÁLIDOS. \n')
        a = float(input('\nERRO! Digite novamente a altura do retângulo: '))
        l = float(input('\nERRO! Digite novamente a largura do retângulo: '))

    conta_largura = 0
    print('')

    while conta_largura < a:
        conta_coluna = 0

        while conta_coluna < l:
            print('*', end='')
            conta_coluna += 1
        print('')
        conta_largura += 1

    pergunta = input('\nDeseja gerar um retângulo? [S] Sim ou [N] Não: ').upper()

print('\nFIM DO PROGRAMA!\n')
