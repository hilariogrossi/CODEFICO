'''O valor aproximado do Pi pode ser calculado usando-se a série: S = 1 - 1/3 ^3 + 1/5^3 - 1/7^3 +
1/9^3 - ...' Sendo Pi = raiz cúbica de S * 32. Faça um programa que calcule e imprima o valor de
Pi usando os 51 primeiros termos da série acima. (for para problema de séries)'''

S = 1
alterna = True

for i in range(3, 103, 2):
    if alterna:
        S -= 1 / (i ** 3)
        alterna = False
    else:
        S += 1 / (i ** 3)
        alterna = True

print(f'\nO valor aproximado de Pi: {(S * 32) ** (1/3)}\n')
