num = input('\nDigite uma lista de número separados por vírgulas: ')

with open('Aula-2/numeros.txt', 'w+') as arquivo:
    arquivo.write(num)

print('\nArquivo Gravado com Sucesso!\n')


with open('Aula-2/numeros.txt', 'r') as arquivo:
    print(f'\nDentro do arquivo: {arquivo.read()}\n')
