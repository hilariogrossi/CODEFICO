# Maior e menor números com fórumlas

a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

c = a + b

if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a

d = maior ** 2 - menor ** 2

if c > d:
    print(f'C foi o maior com valor: {c}.')
else:
    print(f'D foi maior com valor: {d}.')
  
