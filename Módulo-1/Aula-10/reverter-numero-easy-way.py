'''Escreva uma função chamada "reverter_numero" que recebe um número inteiro positivo N como
entrada e retorna o número com os dígitos invertidos. Utilize um loop while para realizar a
inversão. Uma dica é utilizar o operador de resto (%)'''


def reverter_numero(num):
    num_inicio = str(num)
    num_invertido = num_inicio[::-1]

    return num_invertido


numero = int(input('\nDigite um número para a sua inversão: '))

invertido = reverter_numero(numero)

print(f'\nO número {numero} invertido é {invertido}.\n')
