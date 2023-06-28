'''Codificar um programa que leia 3 valores numéricos positivos pelo teclado. O programa deve inicialmente checar se todos os valores são positivos
e caso algum não seja deve solicitar nova entrada de dados. O programa só poderá passar adiante quando os 3 valores informados forem positivos.
O programa deve criar 3 variáveis: maior valor, o segundo maior valor e o menor valor dentre os 3 valores números positivos da entrada.
Ao final imprimir os valores das variáveis menor, meio e maior apresentando-os em ordem crescente.'''

n1 = float(input('\nEntre com primeiro número positivo: '))
n2 = float(input('\nEntre com segundo número positivo: '))
n3 = float(input('\nEntre com terceiro número positivo: '))

while n1 < 0 or n2 < 0 or n3 < 0:
    print('\nVOCÊ ENTROU COM UM NÚMERO NEGATIVO. Repita a operação!')
    n1 = float(input('\nEntre com primeiro número positivo: '))
    n2 = float(input('\nEntre com segundo número positivo: '))
    n3 = float(input('\nEntre com terceiro número positivo: '))

if n1 > n2 > n3:
    maior = n1
    if n2 > n3:
        meio = n2
        menor = n3
    else:
        meio = n3
        menor = n2
elif n2 > n1 > n3:
    maior = n2
    if n1 > n3:
        meio = n1
        menor = n3
    else:
        meio = n3
        menor = n1
else:
    maior = n3
    if n1 > n2:
        meio = n1
        menor = n2
    else:
        meio = n2
        menor = n1

print(f'\nO menor número é o {menor}.\nO número do meio é {meio}, e\nO maior número é {maior}.\n')
