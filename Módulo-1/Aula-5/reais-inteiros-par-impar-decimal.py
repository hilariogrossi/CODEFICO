# Faça um programa que solicita ao usuário informar inicialmente se deseja realizar cálculos com
# valores reais ou inteiros. O usuário deve entrar com '1' para valores inteiros ou '2' para
# valores reais. Caso o valor digitado não seja '1' ou '2', o programa deve ser encerrado.
# Caso contrário, o programa solicita ao usuário que entre com um valor do tipo escolhido.
# No caso de ter escolhido trabalhar com números inteiros, o programa deve informar se o número é
#  par ou ímpar. No caso de ter escolhido trabalhar com número real, o programa deve informar
# a o primeiro digito da parte decimal daquele valor.

print('\n*****Deseja realizar cálculos com valores reais ou inteiros?*****')
tipo = int(input('\n[1] Inteiros ou [2] Reais: '))

if tipo == 1 or tipo == 2:
    if tipo == 1:
        numero = int(input('\nEntre com o número: '))
        if numero % 2 == 0:
            print(f'\nO número digitado "{numero}" é PAR!\n')
        else:
            print(f'\nO número digitado "{numero}" é ÍMPAR!\n')  
    else:
        numero = float(input('\nEntre com o número: '))
        temp = str(numero - int(numero))[2]
        print(f'\nO primeiro digito da da parte decimal é {temp}!\n')
else:
    print('\nNÚMERO DIGITADO NÃO É VÁLIDO. Encerrando o programa...\n')
