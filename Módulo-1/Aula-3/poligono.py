# Implemente um programa para ler a quantidade de lados q (um numero inteiro)
# de um poĺıgono regular, e a medida do lado L(um numero real), classificar o
# polıgono, calcular e imprimir o valor da área (A, com duas casas decimais),
# conforme as descricões a seguir:

# q < 3: "Não é um polígono";
# q = 3: "triângulo" com área: A = (L^2 * √3) / 4;
# q = 4: "quadrado" com área: A = L^2;
# q = 5: "pentágono" com área: A = (5 * L^2) / (4 * tan(0.6283));
# q = 6: "hexágono" com área: A = (3 * L^2 * √3) / 2);
# q > 6: "Polígono não identificado".

# Veja os exemplos de execução a seguir, observe que a medida do lado é
# solicitada apenas quando o polígono é válido, ou seja, primeiro é necessário
#  avaliar a quantidade de lados e:

# (a) Imprimir uma das mensagens de entrada inválida; (b) Solicitar a medida
# do lado e realizar o processamento.

import math

q = int(input('Entre a quantidade de lados do polígono: '))

if q < 3:
    print("\nNão é um polígono\n")
elif q > 6:
    print('\nPolígono não identificado\n')
else:
    L = float(input('Entre com o valor do lado do polígono: '))

    if q == 3:
        area = (L ** 2 * math.sqrt(3) / 4)
        print(f'\nÉ um triângulo e sua área é {area:.2f}\n')
    elif q == 4:
        area = L ** 2
        print(f'\nÉ um quadrado e sua área é {area:.2f}\n')
    elif q == 5:
        area = (5 * L ** 2) / (4 * math.tan(0.6283))
        print(f'\nÉ um pentágono e sua área é {area:.2f}\n')
    elif q == 6:
        area = (3 * L ** 2 * math.sqrt(3) / 2)
        print(f'\nÉ um hexágono e sua área é {area:.2f}\n')
