'''Implemente um programa que receba um número e retorne a quantidade de dígitos desse número.'''

def quantidade_digitos(num):
    num_str = str(num)

    return len(num_str)


numero = int(input('\nEntre com o número: '))

total = quantidade_digitos(numero)

print(f'\nA quandidade de dígitos do número {numero} é {total}.\n')
