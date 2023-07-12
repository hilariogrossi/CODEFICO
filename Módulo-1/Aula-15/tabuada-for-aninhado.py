'''Faça uma tabuada de 1 até 9 utilizando for aninhado.'''

for i in range(1, 10):
    for j in range(1, 10):
        x = i * j
        print(f'{i:2d} X {j:2d} = {x:3d}')
    print('')
