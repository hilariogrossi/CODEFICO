# Trabalhando com with, "w" e "r"

frase = input('\nDigite uma frase: ')

with open('Aula-2/frase.txt', 'w') as arquivo:
    arquivo.write(frase)
print('\nFrase Grava com Sucesso!')

with open('Aula-2/frase.txt', 'r') as arquivo:
    conteudo = arquivo.read()
print(f'\nConteúdo do arquivo: {conteudo}.\n')
