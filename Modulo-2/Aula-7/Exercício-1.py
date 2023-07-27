'''Implemente um programa que receba um dicionário como entrada e retorne o máximo e o mínimo dos 
valores do dicionário. O usuário deverá indicar o final do dicionário fazendo a entrada do valor 0 
para o input Chave.'''

dicionario = {}

while True:
    chave = input('\nEntre com a chave do dicionário: ')

    if chave == '0':
        print('Saindo do Programa...')
        break

    valor = int(input('\nEntre com o valor do dicionário: '))

    dicionario[chave] = valor

maior = max(dicionario.values())
menor = min(dicionario.values())

print(f'\nO valor máximo do dicionário é {maior} e o seu valor mínimo é {menor}.\n')
