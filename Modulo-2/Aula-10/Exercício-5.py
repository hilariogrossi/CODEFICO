'''Implemente uma função que recebe como entrada uma matriz de número inteiros 3x3 e retorna o maior número presenta nessa matriz. Pergunta: qual a complexidade de tempo dessa
função considerando apenas o número de comparações? Entrada: matriz_exemplo = [[3, 12, 5],
                                                                                [2, 8, 4],
                                                                                [9, 6, 7]
                                                                                ]
Saída: Console = O maior número na matriz é o número 9'''


# Exercício 5 - Lista exercício 31/07/2023


def enconta_maior_elemnto(matriz):
    maior_elemento = float('-inf')

    for linha in matriz:
        for elemento in linha:
            if elemento > maior_elemento: # Complexidade 2 * n ** 2 => 2 (for + if) * n (quantidade) * n (for de cima)
                maior_elemento = elemento

    return elemento


def analise_de_complexidade():
    matriz_exemplo = [[3, 12, 5],
                  [2, 8, 4],
                  [9, 6, 7]]

    resultado = enconta_maior_elemnto()
