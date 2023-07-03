'''Faça um programa que converta da notação de 24 horas para a notação de 12 horas e mostre na tela
as horas convertidas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada
em dois inteiros. Use 'A' para representar A.M. e 'P' para representar P.M. A função de conversão
deve receber um valor que indique se é A.M. ou P.M.'''


def converter(hora, minutos):
    if hora > 0 and hora <= 12:
        hora_convertida = hora
        minutos_convertidos = minutos
        print(f'\n{hora_convertida}:{minutos_convertidos} A\n')
    else:
        hora_convertida = hora - 12
        minutos_convertidos = minutos
        print(f'\n{hora_convertida}:{minutos_convertidos} P\n')


H = int(input('\nEntre com as horas no padrão 24 horas: '))
M = int(input('Entre com os minutos: '))

if 0 <= H <= 23 and 0 <= M <= 59:
    converter(H, M)
else:
    print('\nHORA e/ou MINUTOS errado(s). Encerrando o programa.\n')
