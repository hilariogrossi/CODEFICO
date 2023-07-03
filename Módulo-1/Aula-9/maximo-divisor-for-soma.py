'''Dê uma definição para a função maxdiv, que recebe como parâmetro um número inteiro positivo n e
retorna o maior divisor próprio de n. O maior divisor próprio de n é o maior divisor de n diferente
dele próprio. Por exemplo, o maior divisor próprio de 12 é 6 e o maior divisor próprio de 15 é 5.
Escreva agora um programa que leia dois números inteiros e positivos, imprima o maior divisor próprio
de cada um deles e imprima a soma dos maiores divisores próprios desses dois números.'''


def maxdiv(n):
    div = 1

    for i in range(2, int(n / 2 + 2)):
        if n % i == 0:
            divisor = i

    return divisor


print('\nSOMA DOS MAIORES DIVISORES')

valor_1 = int(input('\nDigite um inteiro positivo: '))
resposta_1 = maxdiv(valor_1)
print(f'\nMAIOR DIVISOR PRÓPRIO DE {valor_1} = {resposta_1}.')

valor_2 = int(input('\nDigite um inteiro positivo: '))
resposta_2 = maxdiv(valor_2)
print(f'\nMAIOR DIVISOR PRÓPRIO DE {valor_2} = {resposta_2}.')

soma = resposta_1 + resposta_2

print(f'\nSOMA DOS DIVISORES = {soma}.\n')
