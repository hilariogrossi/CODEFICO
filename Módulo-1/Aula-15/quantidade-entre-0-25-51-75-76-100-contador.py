'''Calcule a quantidade de números nos intervalos (E FORA DELES) [0 - 25], [51 - 75] e [76 - 100], inclusive,
digitados pelo usuário numa entrada contínua até que o mesmo digite um número negativo.'''

contador_0_25 = contador_51_75 = contador_76_100 = contado_fora = 0

numero_usuario = float(input('\nEntre com um número inteiro positivo: [PARA SAIR DIGITE: -1]'))

if numero_usuario < 0:
    print('UM NÚMERO NEGATIVO FOI DIGITADO. SAINDO DO PROGRAMA...')
    exit()

while numero_usuario >= 0:
    if 0 <= numero_usuario <= 25:
        contador_0_25 += 1
    elif 51 <= numero_usuario <= 75:
        contador_51_75 += 1
    elif 76 <= numero_usuario <= 100:
        contador_76_100 += 1
    else:
        contado_fora += 1

    numero_usuario = float(input('\nEntre com um número inteiro positivo: [PARA SAIR DIGITE: -1]'))

print(f'\nA quantidade de números entre [0 - 25] é: {contador_0_25}.')
print(f'\nA quantidade de números entre [51 - 75] é: {contador_51_75}.')
print(f'\nA quantidade de números entre [76 - 100] é: {contador_76_100}.')
print(f'\nA quantidade de números FORA dos intervalos é: {contado_fora}.\n')
