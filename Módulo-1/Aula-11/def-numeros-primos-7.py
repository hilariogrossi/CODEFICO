'''Faça uma nova versão do programa da parte 7, para que use um função como parte da solução. O 
programa principal recebe como entrada uma lista de valores inteiros positivos e para cada um deles
chama a função VerificarPrimo passando o número informado. A função deve retornar 1 se o número
for primo e 0 caso não seja, imprimindo p resultado para cada um dos números da entreda.'''


def VerificarPrimo(numero):
    cont = 2

    while cont <= num / 2:
        if num % cont == 0:
            return 0

        cont += 1


num = int(input('\nDigite um número inteiro e positivo: '))

if num == 1:
    print('\nO número 1 NÃO é primo.\n')
    exit()

while num > 0:
    res = VerificarPrimo(num)

    if res == 0:
        print(f'\nO número {num} NÃO é primo.\n')
    else:
        print(f'\nO número {num} é PRIMO.\n')

    num = int(input('\nDigite um número inteiro e positivo: [DIGITE ZERO (0) PARA SAIR]: \n'))

print('')
