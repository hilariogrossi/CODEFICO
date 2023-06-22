# Implemente um programa que solicite ao usuário um ano e verifique se
# ele é bissexto ou não. Um ano é bissexto se:
# for divisível por 400
# for divisivel por 4 e não for divisível por 100.
# O programa deve exibir uma mensagem indicando se o ano é bissexto ou não.

ano = int(input('Entre com o ano a analisado: '))

if ano % 400 == 0 or (ano % 4 == 0 and ano != 100):
    print(f'O ano {ano} é um ano BISSEXTO.')
else:
    print(f'O ano {ano} NÃO é uma ano bessexto.')
