# Faça um programa que recebe dois valores e impre o maior e o menor

num_1 = float(input('Digite um número: '))
num_2 = float(input('Digite outro número: '))

if num_1 > num_2:
    maior = num_1
    menor = num_2
else:
    maior = num_2
    menor = num_1

print(f'O Menor número é o {menor} e o maior número é o {maior}')
