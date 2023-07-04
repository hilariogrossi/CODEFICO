'''Uma sequência de números pode ser definida a partir de três valores: limite inferior, limite
superior e incremento. A partir do limite inferior esse valor é incrementado interativamente até
atingir ou ultrapassar o limite superior. No caso do valor ultrapassar o limite superior este
último valor não pertence à sequência. Implemente um programa que leia os dois valores de limites
e o incremento. O programa deve imprimir todos os valores que pertencem à sequência que compreenda
o intervalo fechado entre o menor e o maior número conforme limites da entrada. Use somente o while
para implementar as repetições. Caso o valor do incremento seja negatio a sequência deve ser
impressa em ordem decrescente.'''


limite_inferior = float(input('\nEntre com o primeiro número: '))
limite_superior = float(input('\nEntre com o segundo número: '))
incremento = float(input('\nEntre com o valor do incremento: '))

if limite_inferior < limite_superior:
    menor = limite_inferior
    maior = limite_superior
else:
    menor = limite_superior
    maior = limite_inferior

if incremento > 0:
    print('\nValores do Intervalo:')
    while menor <= maior:
        print(f'\n{menor:.1f}')
        menor += incremento
    print('')
elif incremento < 0:
    print('\nValores do Intervalo:\n')
    while maior >= menor:
        print(f'\n{maior:.1f}')
        maior += incremento
    print('')
else:
    print('\nO INCREMENTO NÃO PODE SER ZERO (0)!\n')
