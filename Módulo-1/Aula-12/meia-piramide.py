'''Implemente um programa que irá imprimir uma meia pirâmide. Essa pirâmide está exemplificada nos
exemplos. O programa deve receber a quantidade de níveis que a pirâmide deve ter. O caractere da
pirâmide pode ser qualquer letra, nesse exemplo utilizei a letra "a". Implemente esse programa
utilizando uma função chamada: impimir_piramide(niveis), que recebe a variável "niveis" como
parâmetro.'''


def imprimir_piramide(niveis):
    print('')
    cont = 1
    while cont <= niveis:
        print('a ' * cont)
        cont += 1
    return cont

niveis = int(input('\nQual a quantidade de níveis da pirâmide? '))

imprimir_piramide(niveis)

print('')
