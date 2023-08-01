# Abre o arquivo "arquivo.txt" no modo de leitura ("r")
# Utilizamos read() quando você precisa ler todo o conteúdo do arquivo como uma única string

with open('Aula-2/arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
