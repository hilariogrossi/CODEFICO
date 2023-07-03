'''Escrever um programa principal que lê o valor de um ângulo em graus, x. O valor desse ângulo x
, em radianos, é passado para a Função Definida pelo usuário (COSSENO) a qual calcula o valor do
cosseno de x. O cálculo do cosseno deve ser realizado pela soma dos 100 primeiros termos da série:
cos(x) = 1 - x²/2! + x^4/4! - x^6/6! + x^8/8! - x^10/10! + ... Obs.: A função deve calcular o
cosseno através da série definida acima, não devendo ser usada nenhuma função Python.;'''


import math


def COSSENO(x):
    soma = fatorial = 1

    for i in range(1, 80):
        fatorial *= (i * 2) * (i * 2 - 1)
        fator = x ** (i * 2) / fatorial

        if i % 2 == 0:
            soma += fator
        else:
            soma -= fator

    return soma


angulo_graus = float(input('\nDIGITE O VALOR DE X (GRAUS): '))

radiano = angulo_graus * math.pi / 180

resultado = COSSENO(radiano)

print(f'\ncos({angulo_graus}) = {resultado:.5f}.\n')
