'''Faça uma função que receba um vetor de números reais e retorne três informações em diferentes
variáveis de retorno: - Soma dos valores do vetor; - Média dos valores do vetor; - Maior valor do
vetor; (Conceito utilizado: vetor e função com mais de um retorno)'''

def vetor_real(vetor):
    soma = media = maior = 0

    for i in range(len(vetor)):
        soma += vetor[i]
        media = soma / len(vetor)
        maior = max(vetor)

    return soma, media, maior


vetor_1 = [10, 20, 30 ,40, 50, 15]

soma_1, media_1, maior_1 = vetor_real(vetor_1)

print(f'\nA soma dos elementos do vetor: {soma_1}')
print(f'\nA média dos elementos do vetor: {media_1}')
print(f'\nO maior valor dos elementos do vetor: {maior_1}\n')
