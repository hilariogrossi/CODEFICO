'''Problema do TMA. O tempo médio de atendimento (TMA) de uma central de teleatendimento é calculado
pela média dos tempos de todos os atendimentos realizados em um período. O gerente de uma central 
deseja contratá-lo como analista chefe, porém, para testar suas habilidades de programador, lhe 
propôs o desafio de calcular o tempo médio de atendimento com base em um arquivo texto. O formato 
do arquivo é bastante simples. Cada linha do arquivo contém dois valores inteiros. O primeiro 
representa o momento de início do atendimento, o segundo o momento de fim de atendimento. Cada 
momento é medido em minutos a partir do início do horário do expediente. Faça um programa que leia 
este arquivo e exiba na saída padrão o mínimo, o máximo, a moda e a média com uma casa decimal 
(um valor em cada linha, nesta ordem) do tempo de atendimento.
Algumas considerações:
• Cada momento está no intervalo fechado entre 0 e 1000.
• O arquivo não está ordenado e terá no mínimo uma linha.
• Se não existir moda ou se existir mais de um tempo de atendimento que seja a moda, imprima -1.
• Tempo de atendimento = tempo final - tempo inicial

Exemplo 1
Arquivo: entrada.txt
5 12
6 20
7 8
6 98
11 14
8 25
98 100
56 79
45 98
12 55
1 3
4 6
7 10
10 13
13 16

Saída:
1
92
3
17,9'''

import statistics as st

with open('Aula-3/entrada.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

for i, elemento in enumerate(linhas):
    elemento = elemento.replace('\n', '')

tempo_atendimento = []

for linha in linhas:
    k = []
    k = linha.split()

    tempo_atendimento.append(k)

resultados = []

for e in tempo_atendimento:
    r = int(e[1]) - int(e[0])

    resultados.append(r)

minimo = min(resultados)
maximo = max(resultados)
moda = st.mode(resultados)
media = st.mean(resultados)

print(f'\nO valor mínimo: {minimo} minuto(s).')
print(f'\nO valor máximo: {maximo} minuto(s).')
print(f'\nO valor da moda: {moda}')
print(f'\nO valor da média: {media:.1f} minuto(s).\n')
