# Dados três valores A, B e C, construa um programa para verificar se estes valores podem ser
# valores dos lados de um triângulo.

A = int(input('Entre com o valor do primeiro lado: '))
B = int(input('Entre com o valor do segundo lado: '))
C = int(input('Entre com o valor do terceiro lado: '))

if A <= B + C and B <= A + C and C <= A + B:
    print(f'Os valor digitados {A}, {B} e {C} formam um triângulo.')
else:
    print(f'Os valor digitados {A}, {B} e {C} NÃO formam um triângulo.')
