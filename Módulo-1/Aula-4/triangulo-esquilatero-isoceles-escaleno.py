# Escreva um programa que determine se um triângulo é equilátero, isósceles ou escaleno,
# com base nas medidas dos seus lados fornecidas pelo usuário.
# Dica: Um triângulo equilátero possui todos os lados iguais. Um triângulo isóceles deve possuir
# ao menos dois dos lados iguais. Um triângulo escaleno possui todos os lados diferentes.

a = int(input('Entre com o primeiro lado do triângulo: '))
b = int(input('Entre com o segundo lado do triângulo: '))
c = int(input('Entre com o terceiro lado do triângulo: '))

if a == b == c:
    print('Triângulo Equilátero.')
elif (a == b != c or a == c != b or b == c != a):
    print('Triângulo Isóceles.')
else:
    print('Triângulo Escaleno.')
