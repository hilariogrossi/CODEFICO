'''Escreva um programa que solicite ao usuário um número inteiro positivo e verifique se ele é um
número perfeito. Um número perfeito é aquele cuja soma de todos os seus divisores próprios
(excluindo o próprio número) é igual ao próprio número. Por exemplo, 6 é um número perfeito,
pois 1 + 2 + 3 = 6. (use função)'''


def numero_perfeito(numero):
    soma = 0

    for i in range(1, numero):
        if numero % i == 0:
            soma += i

    if soma == numero:
        return f'\nO número {numero} é um número perfeito.\n'
    else:
        return f'\nO número {numero} NÃO é um número perfeito.\n'


num = int(input('\nEntre com o número: '))

resposta = numero_perfeito(num)

print(resposta)
