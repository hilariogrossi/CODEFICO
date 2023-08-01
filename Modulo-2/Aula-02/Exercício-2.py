# Abre o arquivo "nomes.txt" no modo de leitura ("r")
# Utilizamos readlines() quando é preciso trabalhar com as linhas do arquivo individualmente como elementos de uma lista

with open('Aula-2/nomes.txt', 'r') as arquivo:
    lista_nomes = arquivo.readlines()
    print(lista_nomes)
