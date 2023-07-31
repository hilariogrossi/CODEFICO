def busca_linear(vetor, tamanho, valor):
    existe = 0

    for i in range(tamanho):
        if vetor[i] == valor:
            existe = 1
    return existe
