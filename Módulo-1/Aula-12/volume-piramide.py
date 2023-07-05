'''Implemente um programa que tenha uma FUNÇÃO que calcule o volume de uma pirâmide. Esse programa
deve aceitar como entrada a área da base da piramide(S) e a altura(h).
Volume da pirâmide: (1/3) * S * h'''

def volume_da_piramide(S, h):
    volume_piramide = (1/3) * S * h

    return volume_piramide


base_piramide = float(input('\nDigite a base da pirâmide: '))
altura = float(input('\nDigite a altura da pirâmide: '))

res = volume_da_piramide(base_piramide, altura)

print(f'\nO volume da pirâmide é: {res}\n')
