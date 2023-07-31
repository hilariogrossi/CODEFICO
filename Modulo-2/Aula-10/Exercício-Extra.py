'''Escreva um algoritmo em Python que insira um número extra em uma posição correta dentro de um vetor ordenado, deslocando os outros números, se necessário? 
Qual é a complexidade de tempo desse algoritmo considerando o número de comparações? Exemplo: Entrada: vetor_ordenado = [1, 3, 5, 7, 9]
numero_extra = 6 Console: novo_vetor = [1, 3, 5, 6, 7, 9]'''


def inserir_no_vetor_ordenado(vetor_ordenado, numero_extra):
    indice_insercao = 0

    while indice_insercao < len(vetor_ordenado) and vetor_ordenado[indice_insercao] < numero_extra:
        indice_insercao += 1

    vetor_ordenado.insert(indice_insercao, numero_extra)

    return vetor_ordenado


vetor_ordenado = [1, 3, 5, 7, 9]
numero_extra = 6

print(inserir_no_vetor_ordenado(vetor_ordenado, numero_extra))

# Menor complexidade seria o numero_extra = 0 | f(n) = 1
# Médio caso de complexidade = f(n) = n / 2
# Pior caso = f(n) = n
