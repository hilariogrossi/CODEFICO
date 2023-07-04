'''Escreva uma função chamada "reverter_numero" que recebe um número inteiro positivo N como
entrada e retorna o número com os dígitos invertidos. Utilize um loop while para realizar a
inversão. Uma dica é utilizar o operador de resto (%)'''


def reverter_numero(numero):
    invertido = 0
    while numero > 0:
        resto = numero % 10
        invertido = (invertido * 10) + resto
        numero = numero // 10
    
    return invertido


num = int(input('\nDigite o número a ser invertido: '))
numero_invertido = reverter_numero(num)

print(f'\nO número {num} invertido é {numero_invertido}\n')
