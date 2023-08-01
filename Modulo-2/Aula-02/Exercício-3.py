conteudo = 'Exemplo 2'

with open('Aula-2/arquivo.txt', 'w') as arquivo:
    arquivo.write(conteudo)
    arquivo.seek(0) # Posicionamento do cursor dentro do arquivo.
