'''Escreva uma função que receba uma matriz de carros, onde cada linha representa um carro e contém
suas características (ID, Marca, Placa, Cor, Modelo e Ano de Fabricação). A função deve permitir ao
usuário escolher uma característica do carro e exibir os carros que correspondem a essa caracterís-
tica. Caso não exista nenhum carro com a característica informada, exiba a mensagem: "Nenhum carro
 encontrado com essa característica." Além disso, crie um exemplo de utilização dessa função,
fornecendo a matriz de carros(da questão anterior) e solicitando ao usuário que escolha uma caracte-
rística para realizar a busca.'''

def buscar_caracteristica_carro(matriz):
    escolha = int(input('''\nEscolha uma característica:
    [1] Marca
    [2] Placa
    [3] Cor
    [4] Modelo
    [5] Ano de fabricação\n
    Digite sua opção: '''))

    if 1 <= escolha <= 5:
        caracteristica = input('\nDigite a característica para encontrar um carro: ')
        carro_encontrado = []

        for carro_info in matriz:
            carro = carro_info.split()
            if carro[escolha].lower() == caracteristica.lower():
                carro_encontrado.append(carro)

        if len(carro_encontrado) == 0:
            print('\nNenhum carro encontrado com essa característica.\n')
        else:
            print('\nCarros Encontrados:')
            for carro in carro_encontrado:
                print(f'\n{carro}\n')
    else:
        print('\nOPÇÃO INVÁLIDA!\n')


lista_carros = [
    '0 Porsche YBR7544 Rosa Sport 2015',
    '1 Ford XXX1235 Preto Sport 2019',
    '2 Honda GRE5768 Amarelo Familia 2015',
    '3 Toyota ABC5341 Azul Sport 2022'
]

buscar_caracteristica_carro(lista_carros)
