# Implemente sua primeira calculadora. A calculadora deve conter pelo menos
# as quatro operações básica: soma, subtração, multiplicação e divisão.

print('\n*****Qual operação você deseja fazer?*****')
tipo = int(input('\n[1] Soma, [2] Subtração, [3] Multiplicação e [4] Divisão: \n'))

if 1 <= tipo <= 4:
     num_1 = float(input('Digite o primeiro número para executar a operação: '))
     num_2 = float(input('Digite o segundo número para executar a operação: '))

     if tipo == 1:
          resultado = num_1 + num_2
     elif tipo == 2:
          resultado = num_1 - num_2
     elif tipo == 3:
          resultado = num_1 * num_2
     elif tipo == 4:
          if num_2 != 0:
               resultado = num_1 / num_2
     else:
          print('\nNÃO EXISTE NÚMERO DIVIDIDO POR ZERO (0)! Encerrando o programa...\n')
else:
     print('\nNÃO EXISTE ESSA OPERAÇÃO MATEMÁTICA POR ENQUANTO. Encerrando o programa...\n')

if 1 <= tipo <= 4:
     if num_2 != 0:
          print(f'\nO resultado da sua operação é {resultado:.2f}.\n')
