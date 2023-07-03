'''
O quociente e o resto da divisão inteira de dois números inteiros positivos, A e B,
podem ser calculados por operações sucessivas de subtração.
Por exemplo, se A = 17 e B = 3, a divisão de A por B seria calculada do seguinte modo:
- 1ª subtração:  17 – 3 = 14
- 2ª subtração:  14 – 3 = 11
- 3ª subtração:  11 – 3 = 8
- 4ª subtração:  8 – 3 = 5
- 5ª subtração:  5 – 3 = 2
O quociente da divisão é o número de vezes que foi realizada a subtração de B, neste caso,
5 vezes. Note que a subtração de B é repetida enquanto o resultado obtido é maior ou igual
ao valor de B. O resto da divisão é o resultado obtido na última subtração.
Escreva uma função DivMod, que receba como parâmetros dois números inteiros A e B e retorne
o quociente e o resto da divisão inteira de A por B, calculados conforme a estratégia
explicada acima.
Escreva também um programa principal, que leia dois valores A e B, verifique se os valores
lidos são inteiros positivos e, em caso afirmativo, imprima o quociente e o resto da divisão
de A por B, usando a função DivMod definida anteriormente.
Caso os valores lidos não sejam inteiros, o programa deve imprimir uma mensagem de valores
inválidos e terminar.
(Conceito utilizado: função com duas entradas e duas saídas)
'''

def DivMod(a, b):
    quociente = 0

    while a >= b:
        a -= b
        quociente += 1
        
    return quociente, a


A = int(input('\nEntre com o valor de A: '))
B = int(input('\nEntre com o valor de B: '))

if A >= 0 and B >= 0:
    quociente, a = DivMod(A, B)
else:
    print('Valores inválidos. Terminando o programa...')

print(f'\nO quociente = {quociente} e o resto = {a}!\n')
