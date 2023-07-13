'''Digite 10 números em um vetor e no final imprima a média, o maior e o menor número.'''

import statistics

vetor = []
media = maior = menor = 0

for i in range(10):
    num = int(input(f'\nEntre com o {i + 1}° número do vetor: '))
    vetor.append(num)

media = statistics.mean(vetor)
maior = max(vetor)
menor = min(vetor)

print(f'\nVetor = {vetor}\n')
print(f'\nO menor número do vetor é {menor}.')
print(f'\nO maior número do vetor é {maior}.')
print(f'\nA média dos números do vetor é {media}.\n')
