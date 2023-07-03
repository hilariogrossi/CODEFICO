'''Você foi contratado para desenvolver um programa em Python que faça a conversão de temperatura
de (1)graus Celsius para graus Fahrenheit e (2) graus Celsius para graus Kelvin. Você deve criar
uma função para cada conversão e usuário seleciona qual das duas conversões ele deseja realizar.
Suas funções devem receber como parâmetro a temperatura em graus Celsius e retornar o valor
equivalente em graus Fahrenheit ou Kelvin. Dica: A fórmula usada para transformar graus Celsius
em Fahrenheit é: F = (TC * 9/5) + 32 e para transformar graus Celsius em Kelvin é: K = TC + 273
onde, TC é a temperatura em graus Celsius.'''


def celsiusFahrenheit(TC):
    F = (TC * 9 / 5) + 32

    return F


def celsiusKelvin(TC):
    K = TC + 273

    return K


opcao = int(input('\nConversão [1] Celsius para Fahrenheit e [2] Celsius para Kelvin: '))
while opcao != 1 and opcao != 2:
    opcao = int(input('\nERRO! [1] Celsius para Fahrenheit e [2] Celsius para Kelvin: '))
    
celsius = float(input('\nEntre com a temperatura em Celsius para conversão: '))

if opcao == 1:
    resposta = celsiusFahrenheit(celsius)
    print(f'\nA temperatura {celsius} °C representa {resposta} °F\n')
else:
    resposta = celsiusKelvin(celsius)
    print(f'\nA temperatura {celsius} °C representa {resposta} °K\n')
