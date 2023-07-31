'''Como o seguinte código pode ser melhorado fazendo com que ele faça menos comparações? Apresente a complexidade de tempo das comparações no melhor caso,
caso médio e pior caso da nova implementação Passos: Passo 1: Analisar o código atual; Passo 2: Identificar possíveis comparações nescessárias;
Passo 3: Implementar novamente de forma eficiente; Passo 4: Analisar a complexidade da nova implementação no melhor caso, caso médio e pior caso'''


def max_min(vetor):
    maximo = minimo = vetor[0]

    for i in range(len(vetor)):
        if vetor[i] > maximo:
            maximo = vetor[i]

        else:
            minimo = vetor[i]

    return maximo, minimo

# Exemplo de utilização
vetor_a = [12, 45, 6, 32, 17, 8, 56, 23]
maximo, minimo = max_min(vetor_a)

print(f"Vetor A: {vetor_a}\nMáximo: {maximo}\nMínimo: {minimo}")

# melhor caso = Ordem crescente ; Caso médio = ordem decrescente; Caso ruim = Buscar todos
