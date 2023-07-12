'''Faça um programa que mostre a tabuada (de 1 a 10) de vários números, um de cada vez, para cada
valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
O programa deve realizar as seguintes etapas:
1.   Solicitar ao usuário que digite um número inteiro positivo.
2.   Verificar se o número digitado é negativo. Se for, interromper o programa..
3.   Se o número for positivo, calcular e exibir a tabuada desse número.
4.   Voltar ao passo 1 e repetir o processo até que um número negativo seja digitado.'''

while True:
    numero = int(input('\nInforme um número inteiro positivo para tabuada [1 - 10]: '))

    if numero < 0:
        print('\nEncerrando o programa...\n')
        break
    elif numero > 10 or numero == 0:
        print('\nERRO! O intervalo aceitável é de 1 a 10.\n')
        break

    print(f'\n***** TABUADA DO NÚMERO {numero} *****\n')

    for i in range(1, 11):
        total = i * numero

        print(f'{i:2d} X {numero:2d} = {total:3d}')

print()
