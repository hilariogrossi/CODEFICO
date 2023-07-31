def cria_matriz(n):
    matriz = []

    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)
    
    return matriz
