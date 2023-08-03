'''A busca binária é um algoritmo de busca eficiente usado para encontrar um elemento específico em
uma lista ordenada. O algoritmo divide repetidamente a lista ao meio, eliminando metade dos 
elementos em cada iteração, até que o elemento desejado seja encontrado ou a sublista se torne 
vazia. Pergunta: Qual a ordem (classe) de complexidade da busca binária no seguinte código?'''

def busca_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

# Exemplo de uso:
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15]
alvo = 7

posicao_binaria = busca_binaria(lista_ordenada, alvo)

if posicao_binaria != -1:
    print(f"\nO alvo {alvo} foi encontrado na posição {posicao_binaria}.\n")

else:
    print(f"\nO alvo {alvo} não foi encontrado na lista.\n")
