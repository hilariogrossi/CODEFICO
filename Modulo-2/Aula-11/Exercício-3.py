'''Escreva um algoritmo que receba valores em um vetor e imprima “ORDENADO” se o vetor estiver em
ordem crescente. Qual e função de custo de pior caso e sua ordem de complexidade O?
Entrada: vetor = [1, 3, 5, 7, 9] Saída: Console = ORDENADO'''

def ordenado(v):
    for i in v:
        if v[i] < v[i + 1]:
            return True

    return False


vetor = [1, 3, 5, 7, 9]

if ordenado(vetor):
    print('\nORDENADO\n')

else:
    print('\nNÃO ordenado\n')
