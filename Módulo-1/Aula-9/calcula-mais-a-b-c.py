'''Faça uma função calculaMais que recebe três parâmetros a, b, c. Caso o terceiro parâmetro (c)
seja 0 a função deve fazer a subtração de a por b e retornar. Caso contrário a função faz a soma dos
três valores e retorna o resultado. Faça a função principal para solicitar os valores a serem
repassados para a função calculaMais e para imprimir o resultado a operação.'''


def calculaMais(a, b, c):
    if c == 0:
        res = a - b
    else:
        res = a + b + c

    return res


a = float(input('\nEntre com o valor de A: '))
b = float(input('\nEntre com o valor de B: '))
c = float(input('\nEntre com o valor de C: '))

resposta = calculaMais(a, b, c)

print(f'\nO resultado da operação é {resposta}.\n')
