'''Criar um programa que solicita uma string e verifica se ela é um palíndromo ou não. Um palíndromo
é uma string que, quando invertida, se mantém igual a original. Por exemplo: arara.'''

texto = input('\nEntre com o texto para verificação se é um palíndromo: ')

if texto == texto[::-1]:
    print(f'\nO texto digitado {texto} é um palíndromo ({texto[::-1]}).\n')
else:
    print(f'\nO texto digitado {texto} NÃO é um palíndromo ({texto[::-1]}).\n')
