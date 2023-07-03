'''Elabore uma função que calcula a distância euclidiana entre dois pontos bidimensionais. A função
recebe as coordenadas x e y de dois pontos e gera o resultado, retornando o valor para a função
principal, e em seguida, o imprime na tela. Utilizar x1, x2, y1 e y2 como argumentos(parâmentros)
da função. DICAS: (1)a fórmula da distancia entre dois pontos é:
D =  RAIZ(x1 - x2)² + (y1 - y2)²
onde: x1, y1 e x2, y2 são as coordenadas dos pontos, respectivamente.
Ex: p1 = (x1,y1) p2(x2,y2)
------------------------------------------------------------------------------------------------------------------------------
(2) Use a função math.sqrt() para calcular a raíz quadrada.'''

import math


def calculaDistancia(x1, x2, y1, y2):
    D = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return D


X1 = int(input('\nEntre com o valor de X1: '))
X2 = int(input('\nEntre com o valor de X2: '))
Y1 = int(input('\nEntre com o valor de Y1: '))
Y2 = int(input('\nEntre com o valor de Y2: '))

resposta = calculaDistancia(X1, X2, Y1, Y2)

print(f'\nA distância entre dois pontos é: {resposta:.2f}\n')
