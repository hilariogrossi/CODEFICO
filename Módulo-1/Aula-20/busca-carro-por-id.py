'''Implemente uma função chamada buscar_carro_por_id que receba como parâmetros uma matriz de
carros e um ID de carro a ser buscado. A função deve buscar o carro na matriz pelo ID e retornar o
carro encontrado. O funcionamento da função pode seguir os seguintes passos:
Receber como argumentos a matriz de carros e o ID do carro a ser buscado.
Percorrer a matriz de carros e verificar se o ID do carro em cada linha é igual ao ID fornecido.
Se o ID do carro for encontrado, retornar o carro encontrado.
Caso contrário, retornar None para indicar que o carro não foi encontrado.'''

def buscar_carro_por_id(matriz_de_carros, id_carro):
    for carro in matriz_de_carros:
        if carro[0] == id_carro:
            return carro
    return None


id = input('\nForneça o ID para buscar o carro: ')

lista_carros = [
    ['0', 'Porsche', 'YBR7544', 'Rosa', 'Sport', '2015'],
    ['1', 'Ford', 'XXX1235', 'Preto', 'Sport', '2019'],
    ['2', 'Honda', 'GRE5768', 'Amarelo', 'Familia', '2015'],
    ['3', 'Toyota', 'ABC5341', 'Azul', 'Sport', '2022']
]

carro_encontrado = buscar_carro_por_id(lista_carros, id)

if carro_encontrado:
    print(f'\nCARRO ENCONTRADO:\n ID {carro_encontrado}\n')
else:
    print('\nCARRO NÃO ENCONTRADO.\n')
