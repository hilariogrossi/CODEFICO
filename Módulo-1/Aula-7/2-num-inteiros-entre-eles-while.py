'''Implemente um código que peça dois números e imprima todos os inteiros entre esses dois números.
Cuidado: Caso sua condição de parada não seja boa seu while entrará em loop indefinido.'''

n1 = int(input('\nEntre com primeiro número inteiro: '))
n2 = int(input('\nEntre com segundo número inteiro: '))

if n1 < n2:
    while n1 <= n2:
        print(f'\n{n1}\t')
        n1 += 1
else:
    while n2 <= n1:
        print(f'\n{n2}\n')
        n2 += 1
 
