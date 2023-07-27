'''Implemente um programa que receba uma string e retorne um dicionario com as chaves como os 
caracteres e os valores como a quantidade de vezes aquele caractere aparece na string.
Exemplo 1 - Entrada: String: Hello, World! Saída: { 'H': 1, 'e':1, 'l':3, 'o':2, ,',':1, 'w':1, 'r':1, 'd':1, '!': 1 }'''


def contar_caracteres(string):
    dicionario = {}

    for caracter in string:
        if caracter != ' ': # Se não quiser contar o espaço
            if caracter in dicionario:
                dicionario[caracter] += 1
            else:
                dicionario[caracter] = 1
    return dicionario


entrada = "Hello, World!"
# entrada = input('\nEntre com a frase: ')

saida = contar_caracteres(entrada)

print(saida)
