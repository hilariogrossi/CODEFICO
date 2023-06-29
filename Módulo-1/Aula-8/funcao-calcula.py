'''Faça uma função chamada Calcula, que recebe tres parâmetros: dois números a e b,
e uma string para representar a operação a ser realizada entre os números a e b.
São três operações permitidas: soma, subtração e multiplicação. A função deve retornar
o resultado da operação escolhida sobre os números a e b. Caso não seja informada uma
opção válida, deve retornar o valor -999.
Faça também um programa principal (função principal) que solicite ao usuário os valores
de a e b e também a operação, chamando a função criada com os parâmetros, e imprima o
resultado da operação ou uma mensagem de erro caso a operação não seja válida.
(Conceito utilizado: nossa primeira função)'''

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
oper = input('\nEntre com a operação [soma, subtracao, multiplicacao ou divisao]: ').lower()

resp = calcula(A, oper, B)

if resp == -999:
    print('\nOPERAÇÃO INVÁLIDA!\n')
else:
    print(f'\nA resposta para a operação "{oper}" é {resp}.\n')
