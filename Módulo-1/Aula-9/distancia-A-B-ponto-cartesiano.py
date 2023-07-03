'''A distância entre dois pontos A e B no plano cartesiano pode ser pela fórmula:
distância = math.sqrt((Xb - Xa)² + (Yb - Ya)²). Escreva um programa principal e uma função definida
pelo usuário DIST, onde: [1] O programa principal faz a leitura das coordenadas dos pontos A e B, ou
seja, os valores de Xa, Ya, Xb e Yb conforme o exemplo de execução abaixo; [2] O programa principal
faz a chamada a uma função DIST com os valores das coordenadas lidas. A função retorna para o
programa principal o valor numérico da distância entre os pontos A e B. [3] O programa principal
faz a impressão da distância calculada. Obs.: não é necessária a validação dos dados de entrada.
As coordenadas serão sempre números reais.'''


import math


def DIST(xa, ya, xb, yb):
    resposta = (xb - xa) ** 2 + (yb - ya) ** 2
    return math.sqrt(resposta)


print('\n*****CÁLCULO DA DISTÂNCIA ENTRE DOIS PONTOS*****\n')

XA = float(input('\nINFORME XA: '))
YA = float(input('\nINFORME YA: '))
XB = float(input('\nINFORME XB: '))
YB = float(input('\nINFORME YA: '))

distancia = DIST(XA, YA, XB, YB)

print(f'\nDistância ({XA}, {YA}) e ({XB}, {YB}) = {distancia}!\n')
