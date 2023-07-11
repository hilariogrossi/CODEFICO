'''Utilizando a estrutura de repetição for, faça um programa em Linguagem Python que receba 10
números e conte quantos deles estão no intervalo [10,20] (incluso) e quantos deles estão fora do
intervalo, escrevendo estas informações.'''

incluso = fora = 0

for i in range(1, 11):
    num = int(input(f'\nEntre com o {i}° número: '))
    if 10 <= num <= 20:
        incluso += 1
    else:
        fora += 1

print(f'\nA quantidade de números dentro do intervalo [10 - 20] é {incluso} |\n')
print(f'\nA quantidade de números fora do intervalo [10 - 20] é {fora} |\n')
