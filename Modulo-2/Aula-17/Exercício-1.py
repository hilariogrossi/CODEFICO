# Soma quadrados dos números

def soma_quadrados(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    return n ** 2 + soma_quadrados(n - 1)


numero = int(input('\nEntre com o número: '))

res = soma_quadrados(numero)

print(f'\nA soma dos quadrados do número {numero} é ==> {res}.\n')
