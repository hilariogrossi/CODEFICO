'''Crie uma função chamada "soma_primos" que recebe um número inteiro
positivo N como entrada e retorna a soma de todos os números primos menores
ou iguais a N. Uma dica é fazer outra função para verificar se o número é primo'''


def verifica_primos(num):
    div = 0
    cont = 1

    while cont <= num:
        if num % cont == 0:
            div += 1
        cont += 1

    if div == 2:
        return True
    else:
        return False


def soma_primos(n):
    soma = 0
    inicio = 2

    while inicio <= n:
        if verifica_primos(inicio):
            soma += inicio
        inicio += 1

    return soma


numero = int(input('\nEntre com o número para verificação: '))

soma_final = soma_primos(numero)

print(f'\nA soma dos números primos do número {numero} é {soma_final}.\n')
