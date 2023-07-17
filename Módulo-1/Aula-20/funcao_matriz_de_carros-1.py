'''Escreva uma função que permita a criação de uma matriz de carros a partir de uma lista de strings.
Cada string na lista representa as informações de um carro, incluindo um Indentificador unico(ID),
Marca, Placa, Cor, Modelo e Ano de Fabricação. O programa deve processar a lista de strings e 
preencher a matriz de carros com as informações correspondentes. A função deve receber como 
argumento a lista de strings contendo as informações dos carros e retornar a matriz de carros
preenchida.Siga este modelo: ID na posição [i] [0], Marca na posição [i] [1], Placa na posição 
[i] [2], Cor na posição [i] [3], Modelo na posição [i] [4] e Ano de Fabricação na posição [i] [5].
Passo a passo para criar uma matriz de carros a partir de uma lista de strings:
1. Defina uma função chamada `criar_matriz_carros` que recebe como argumento a lista de strings
contendo as informações dos carros.
2. Inicialize uma matriz vazia chamada `matriz_carros`.
3. Crie um loop para percorrer cada string na lista de carros.
4. Dentro do loop, divida a string em substrings utilizando o método `split()` e armazene o 
resultado em uma variável chamada `carro`.
5. Adicione a lista `carro` à matriz `matriz_carros`.
6. Retorne a matriz `matriz_carros` preenchida com as informações dos carros.'''

def criar_carros(lista_carros):
    matriz_carros = []

    for carro_info in lista_carros:
        carro = carro_info.split()
        matriz_carros.append(carro)

    return matriz_carros


lista_carros = [
    '0 Porsche YBR7544 Rosa Sport 2015',
    '1 Ford XXX1235 Preto Sport 2019',
    '2 Honda GRE5768 Amarelo Familia 2015',
    '3 Toyota ABC5341 Azul Sport 2022'
]

print('\n')

for i in criar_carros(lista_carros):
    print(f'{i}')
    
print('\n')
