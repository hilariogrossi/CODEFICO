'''
Crie um novo arquivo para usar a função Calcula definida no programa da Parte 1.
Para este novo programa, faça um laço while para que o usuário entre com quantas
rodadas de valores desejar, devendo informar o parâmetro de opção = "parar" caso
deseje terminar o programa. Enquanto o programa não for terminado, a função Calcula
deve ser chamada e ter seu resultado impresso no programa principal, para cada conjunto
de valores da entrada.
(Conceito utilizado: função como parte de uma biblioteca e com múltiplas chamadas)
'''

def calcula(a, operacao, b):
    if operacao == 'soma' or operacao == '+':
        resposta = a + b
    elif operacao == 'subtracao' or operacao == '-':
        resposta = a - b
    elif operacao == 'multiplicacao' or operacao == '*':
        resposta = a * b
    elif operacao == 'divisao' or operacao == '/':
        if a != 0 and b != 0:
            resposta = a / b
        else:
            print('\nVerifique se o número  é zero (0)!\n')
            resposta = -999
    else:
        resposta = -999

    return resposta


A = float(input('\nEntre com o valor de A: '))
B = float(input('\nEntre com o valor de B: '))
print('\nDigite "PARAR" para parar o programa.')
oper = input('\nEntre com a operação [soma, subtracao, multiplicacao ou divisao]: ').lower()

while oper != 'parar':
    resp = calcula(A, oper, B)

    if resp == -999:
        print('\nOPERAÇÃO INVÁLIDA!\n')
    else:
        print(f'\nA resposta para a operação "{oper}" é: {resp}.\n')

    A = float(input('\nEntre com o valor de A: '))
    B = float(input('\nEntre com o valor de B: '))
    oper = input('\nEntre com a operação [soma, subtracao, multiplicacao ou divisao]: ').lower()

print('\n************************************************************\n')
