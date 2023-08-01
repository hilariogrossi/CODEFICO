with open('Aula-2/numeros.txt', 'r') as arquivo:
    conteudo = arquivo.read()

numeros_str = conteudo.split(',')
numeros_int = []

for n in numeros_str:
    numeros_int.append(int(n))

print(f'\nA lista de números é {numeros_int}.\n')
