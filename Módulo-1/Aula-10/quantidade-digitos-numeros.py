'''Escreva uma função chamada "quantidade_digitos" que recebe um número
inteiro positivo N como entrada e retorna a quantidade de dígitos desse
número.'''


def quantidade_digitos(n):
    numero_str = str(n)
    return len(numero_str)


num = int(input('\nDigite o número para verificação: '))

resposta = quantidade_digitos(num)

print(f'\nA quantidade de dígitos do número {num} é: {resposta}\n')
