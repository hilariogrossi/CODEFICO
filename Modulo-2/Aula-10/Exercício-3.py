'''Escreva um algoritmo que receba uma lista de números e um valor de busca, retornando True se o valor estiver presente na lista e False caso contrário.
Pergunta: Qual é a complexidade de tempo do seu algoritmo considerando apenas as comparações? Exemplo:  Entrada: Lista: [10, 25, 32, 45, 50, 62, 70]
Valor procurado: 45 Saída: Console: O valor 45 está presente na lista'''


def busca_numero(vetor, tamanho, valor):
    for i in range(tamanho):
        if vetor[i] == valor:
            return True
    return False


lista = [10, 25, 32, 45, 50, 62, 70]
valor_procurado = 45
tamanho = len(lista)

if busca_numero(lista, tamanho, valor_procurado):
    print(f'\nO valor {valor_procurado} está presente na lista.\n')
else:
    print(f'\nO valor {valor_procurado} NÃO está presente na lista.\n')

# Complexidade f(n) = 2 * n + 1
