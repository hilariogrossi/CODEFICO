'''Crie um programa que armazena diversos inteiros em uma lista e depois os imprime em ordem de
tamanho, cada número em uma linha.'''

lista_numeros = []

quantidade_numeros = int(input('\nQual a quantidade de números deseja guardar: '))

for i in range(quantidade_numeros):
    numero = int(input(f'\nEntre com o {i + 1}° número: '))
    lista_numeros.append(numero)

ordem_de_tamanho = sorted(lista_numeros)

print(f'\nLista de números: {lista_numeros}\n')
print(f'A ordem de tamanho da lista é {ordem_de_tamanho}.\n')
