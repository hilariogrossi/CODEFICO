# Faça um programa que solicita ao usuário informar inicialmente se deseja realizar cálculos com valores "reais" ou "inteiros".
# O usuário deve entrar com "real" ou "inteiro" e caso o texto digitado não seja um destes dois o programa deve ser encerrado. Caso contrário o programa
# solicita ao usuário que entre com um valor do tipo escolhido. No caso de ter escolhido trabalhar com número inteiro positivo e faça com que o
# programa imprima todos os números em ordem decrescente, ou seja, do valor informado até zero. Imprimir inteiros com espaço para números de 5 dígitos.
# No caso de ter escolhido trabalhar com número real o programa deve imprimir o número contendo 7 dígitos no total sendo 2 dígitos para a parte decimal.
# While para garantir entrada válida

tipo = input('Entre com com a palavra "real" caso queira númerios reais ou a palavra "inteiro" caso queira números inteiros: ').lower()

while tipo != 'inteiro' and tipo != 'real':
    tipo = input('\nEntrada inválida. Digite real ou inteiro: ')

if tipo == 'inteiro':
    num = int(input('\nEntre com o número para ser processado: '))
    cont = num
    while cont >= 0:
        print(f'{cont:5d}')
        cont -= 1
else:
    num = float(input('Entre com o número para ser processado: '))
    print(f'{num:7.2f}')
