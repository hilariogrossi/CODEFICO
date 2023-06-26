# Faça um programa que solicita ao usuário informar inicialmente se deseja realizar cálculos com valores "reais" ou "inteiros".
# O usuário deve entrar com "real" ou "inteiro" e caso o texto digitado não seja um destes dois o programa deve ser encerrado. Caso contrário o programa
# solicita ao usuário que entre com um valor do tipo escolhido. No caso de ter escolhido trabalhar com número inteiro o programa deve informar se o número
# é par ou ímpar. No caso de ter escolhido trabalhar com número real o programa deve isolar o primeiro dígito da parte decimal e veificar se ele
# representa um número par ou ímpar.
# PARA ESTE PROGRAMA SEPARAR A PARTE DE PROCESSAMENTE E SAÍDA USANDO UMA VARIÁVEL DO TIPO BOOLEANO.

tipo = input('Digite inteiro ou real para prosseguir: ').lower()

if tipo != 'inteiro' and tipo != 'real':
    print('VOCÊ NÃO DIGITOU CORRETAMENTE. Encerrando o programa...')
else:
    if tipo == 'inteiro':
        num = int(input('Entre com número para processamento: '))
        if num % 2 == 0:
            resposta_booleana = True
        else:
            resposta_booleana = False
    else:
        num = float(input('Entre com o número para processamento: '))
        temp = str(num - int(num))[2]
        if int(temp) % 2 == 0:
            resposta_booleana = True
        else:
            resposta_booleana = False
    
    if resposta_booleana:
        print('O número é PAR!')
    else:
        print('O número é ÍMPAR!')
