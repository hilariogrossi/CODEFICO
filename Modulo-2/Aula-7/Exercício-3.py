'''Receba um dicionario com os nomes do alunos e suas notas, após isso retorne a média da nota dos 
alunos. Deve ser possível adicionar N alunos. Para definir a parada o input Aluno deve receber o 
valor 0.'''

import statistics as st


def media_alunos(dicionarios):
    media = st.mean(dicionarios.values())

    return media


i = 1
dicionario = {}

while True:
    aluno = input(f'\nEntre com o nome do {i}° aluno: ')

    if aluno == '0':
        print('\nSaindo do programa. Obrigado por utilizar o Hilário´s APP!')
        break

    notas = float(input(f'\nEntre com a nota do {i}° aluno: '))

    dicionario[aluno] = notas

    i += 1

resultado = media_alunos(dicionario)

print(f'\nA media das notas dos alunos é: {resultado}.\n')
