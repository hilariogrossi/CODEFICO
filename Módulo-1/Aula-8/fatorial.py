'''Escreva uma função que calcule o fatorial de um número inteiro. O fatorial de um número é o
produto de todos os números inteiros positivos menores ou iguais a ele. Por exemplo, o fatorial
de 5 é calculado como 5 * 4 * 3 * 2 * 1, resultando em 120. A função deve receber um número inteiro
como parâmetro e retornar o valor do fatorial.'''


def fatorial(num):
    fat = 1

    while num > 1:
        fat *= num
        num -= 1
 
    return fat


numero = int(input('\nEntre com o número para fatoração: '))

if numero < 0:
    print('\nNÃO EXISTE FATORIAL DE NÚMERO NEGATIVO!\n')
else:
    resposta = fatorial(numero)
    print(f'\nO faotial do número {numero} é: {resposta}.\n')
