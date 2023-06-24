# Escreva um programa em Python que converta uma temperatura em graus Celsius para Fahrenheit ou
# vice-versa, com base na escolha do usuário. Para converter de Celsius para Fahrenheit você
# precisa multiplicar o valor da temperatura por 1.8 e somar 32. Para converter de Fahrenheit
# para Celsius você precisa subtrair o valor da temperatura por 32 e dividir por 1.8
# 1.8 em fração é 9/5

print('\n*****Qual conversão você deseja fazer*****\n')
tipo = int(input('\n[1] Celsius para Fahrenheit ou [2] Fahrenheit para Celsius: \n'))

if tipo == 1 or tipo == 2:
     if tipo == 1:
        celsius = float(input('Digite o valor a ser convertido de Celsius para Fahrenheit: '))
        resultado = celsius * 1.8 + 32
     else:
        fahrenheit = float(input('\nDigite o valor a ser convertido de Fahrenheit para Celsius: \n'))  
        resultado = (fahrenheit - 32) / 1.8  
     
     print(f'\nO resultado da sua conversão é {resultado:.2f}!\n')
else:
    print('\nNÃO EXISTE ESSE TIPO DE CONVERSÃO! Encerrando o programa...\n')
