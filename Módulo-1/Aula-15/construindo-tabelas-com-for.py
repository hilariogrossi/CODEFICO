'''Aprendendo mais sobre construção de tabelas com o for'''

x = int(input('\nDigite o valor de x: '))
y = int(input('\nDigite o valor de y: '))

print()

print('', end='')

for col in range(x, y + 1):
    print(f'{col:3d}   ', end='')

print()

print('-----', end='')

for col in range(x, y + 1):
    print('-----', end='')

print()

for lin in range(x, y + 1):
    print(f'{lin:3d}   ', end='')

print()

for lin in range(x, y + 1):
    print(f'{lin:3d}   ', end='')
