'''Faça um programa que imprime, entre 1 e 1.000.000, o primeiro número que
é divisível por 11,13 e 17. Uso do break'''

for num in range(1, 1000000 + 1):
    if num % 11 == 0 and num % 13 == 0 and num % 17 == 0:
        print(f'\nO primeiro número do intervalo que é divisível por 11, 13 e 17 ao mesmo tempo é {num}.\n')
        break
