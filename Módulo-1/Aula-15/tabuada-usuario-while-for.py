'''Faça um programa para produção de uma tabuada informada pelo usuário usando while e for com a
condição de parada com um número negativo.'''

while True:
    numero = int(input('\nEntre com um número de 1 a 10 para a produção da tabuada: '))

    if numero < 0:
        print('\nEncerrando o programa...\n')
        break
    elif numero == 0:
        print('\nA tabuada do zero (0) sempre terá como resultado zero (0).\n')
        break
    elif numero > 10:
        print('\nHoje não produziremos tabuadas com valores maiores do que 10.\n')
        break

    print(f'\nTABUADA DO NÚMERO {numero}!\n')

    for i in range(1, 11):
        produto = i * numero
        print(f'{i:2d} X {numero:2d} = {produto:3d}')

    print()
