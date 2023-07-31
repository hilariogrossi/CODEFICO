def busca_linear_2(vetor, tamanho, valor):
    for i in range(tamanho):
        if vetor[i] == valor:
            return 1
    return 0
