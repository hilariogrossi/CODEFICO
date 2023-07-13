'''Faça uma função que leia uma palavra e descubra é ela é ou não um palíndromo. Como abaixo:
Criar um programa que solicita uma string e verifica se ela é um palíndromo ou não. Um
palíndromo é uma string que, quando invertida, se mantém igual a original. Por exemplo: arara.'''

def palindromo(texto):
    if texto == texto[::-1]:
        return True
    else:
        return False


print('\n***** PALÍNDROMO? *****')
texto_entrada = input('\nEntre com a palavra ou frase para verificação: ')

resposta = palindromo(texto_entrada)

if resposta:
    print('\nO texto de entrada é um palíndromo.\n')
else:
    print('\nO texto de entrada NÃO é um palíndromo.\n')
