def busca_linear_3(vetor, tamanho, valor):
    vetor.append(valor)

    i = 0

    while vetor[i] != valor:
        i += 1

    if i < tamanho:
        return 1

    return 0
