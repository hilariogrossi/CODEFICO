'''Desenvolva uma função chamada marca_carro_alugado que recebe uma matriz de carros e o ID de um 
carro que foi alugado. A função deve percorrer a matriz de carros, localizar o carro com o ID 
fornecido e marcar esse carro como alugado, adicionando a string "Alugado" ao final da linha desse
carro. Em seguida, a função deve retornar a matriz de carros atualizada. A matriz de carros é uma
lista de listas, onde cada lista representa as informações de um carro. As informações do carro são:
ID, Marca, Placa, Cor, Modelo, Ano de Fabricação.
Segue o exemplo de entrada e saída para o código fornecido:
Matriz de carros:
[
    ['0', 'Porsche', 'YBR7544', 'Rosa', 'Sport', '2015'],
    ['1', 'Ford', 'XXX1235', 'Preto', 'Sport', '2019'],
    ['2', 'Honda', 'GRE5768', 'Amarelo', 'Familia', '2015'],
    ['3', 'Toyota', 'ABC5341', 'Azul', 'Sport', '2022']
]

ID do carro alugado: '1'

Matriz de carros atualizada:
[
    ['0', 'Porsche', 'YBR7544', 'Rosa', 'Sport', '2015'],
    ['1', 'Ford', 'XXX1235', 'Preto', 'Sport', '2019', 'Alugado'],
    ['2', 'Honda', 'GRE5768', 'Amarelo', 'Familia', '2015'],
    ['3', 'Toyota', 'ABC5341', 'Azul', 'Sport', '2022']
]
Nesse exemplo, o carro com ID '1' foi marcado como alugado na matriz de carros. A informação 
"Alugado" foi adicionada ao final da linha desse carro. A matriz de carros atualizada é exibida,
mostrando que o carro com ID '1' está marcado como alugado.'''


def marca_carro_alugado(matriz_carros, id_carro):
    for carros in matriz_carros:
        if carros[0] == id_carro:
            carros.append("Alugado")
    return matriz_carros


matriz_carros = [
    ['0', 'Porsche', 'YBR7544', 'Rosa', 'Sport', '2015'],
    ['1', 'Ford', 'XXX1235', 'ROSA', 'Sport', '2019'],
    ['2', 'Honda', 'GRE5768', 'Amarelo', 'Familia', '2015'],
    ['3', 'Toyota', 'ABC5341', 'Azul', 'Sport', '2022']
]

id = '3'

matriz_carros = marca_carro_alugado(matriz_carros, id)

print('\n')

for carro in matriz_carros:
    print(carro)

print('\n')
