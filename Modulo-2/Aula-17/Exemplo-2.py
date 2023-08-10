# Soma dígitos


def soma_digitos(n):
    if n < 10:
        return n

    return soma_digitos(n // 10) + (n % 10)


numero = int(input('\nEntre com o número para contagem de dígitos: '))

res = soma_digitos(numero)

print(f'\nA soma dos dígitos do número {numero} é: {res} |\n')
