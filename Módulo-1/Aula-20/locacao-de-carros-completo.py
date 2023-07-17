'''Implemente um programa que utilize as funções das questões anteriores para criar um programa 
completo de locadora de carros. A função deve exibir um menu de opções para o usuário, onde ele 
pode escolher criar uma locação, exibir todas as locações realizadas, buscar um carro por sua 
característica ou sair do programa. O programa deve executar até que o usuário escolha a opção de 
sair. Considere que todas entradas serão validas.
--- MENU ---
1. Criar locação
2. Exibir locações
3. Buscar Carro
0. Sair

Escolha uma opção: 1

Digite o nome do cliente: Joelison

Digite a data da locação: 13-07

Digite a quantidade de carros a serem alugados: 1

Carros disponíveis para locação:

ID: 0, Marca: Porsche, Placa: YBR7544, Cor: Rosa, Modelo: Sport , Ano: 2015
ID: 1, Marca: Ford, Placa: XXX1235, Cor: Preto, Modelo: Sport , Ano: 2019
ID: 3, Marca: Honda, Placa: GRE5768, Cor: Amarelo, Modelo: Familia , Ano: 2015
ID: 5, Marca: Toyota, Placa: ABC5341, Cor: Azul, Modelo: Sport , Ano: 2022

Digite o ID do 1º carro a ser alugado: 5

Locação criada com sucesso!

--- MENU ---
1. Criar locação
2. Exibir locações
3. Buscar Carro
0. Sair
Escolha uma opção: 2

# Saida
['Joelison', '13-07', 1, [['5', 'Toyota']]]

--- MENU ---
1. Criar locação
2. Exibir locações
3. Buscar Carro
0. Sair
Escolha uma opção: 3

Escolha uma característica para buscar um carro:
1. Marca
2. Placa
3. Cor
4. Modelo
5. Ano de Fabricação

Opção: 5
Digite a característica: 2015

Carros encontrados:
['0', 'Porsche', 'YBR7544', 'Rosa', 'Sport', '2015']
['3', 'Honda', 'GRE5768', 'Amarelo', 'Familia', '2015']

--- MENU ---
1. Criar locação
2. Exibir locações
3. Buscar Carro
0. Sair

Escolha uma opção: 0

Programa encerrado.'''


def criar_matriz_carros(lista_carros):
    matriz_carros = []
    for carro_info in lista_carros:
        carro = carro_info.split()
        matriz_carros.append(carro)
    return matriz_carros


def buscar_carro_por_id(matriz_carros, id_carro):
    for carro in matriz_carros:
        if carro[0] == id_carro:
            return carro
    return None


def marca_carro_alugado(matriz_carros, id_carro):
    for carro in matriz_carros:
        if carro[0] == id_carro:
            carro.append('Alugado')
    return matriz_carros


def cria_locacao(matriz_carros):
    locacao = []
    nome_cliente = input("\nDigite o nome do cliente: ")
    data_locacao = input("\nDigite a data: ")
    qtd_carros = int(input("\nDigite a quantidade de carros que deseja alugar: "))

    print("\nCarros disponveis para locação:")
    for carro in matriz_carros:
        if len(carro) <= 6:
            print(f"\nID: {carro[0]}, Marca: {carro[1]}, Placa: {carro[2]}, Cor: {carro[3]}, Modelo: {carro[4]}, Ano: {carro[5]}")

    carros_escolhidos = []

    for i in range(qtd_carros):
        id = input(f"Digite o ID do {i + 1}° carro: ")

        carro_escolhido = buscar_carro_por_id(matriz_carros, id)
        if len(carro_escolhido) > 6 and carro_escolhido[6] == 'Alugado':
            print("\nCarro escolhido já está alugado!\n")
        else:
            carros_escolhidos.append([carro_escolhido[0],carro_escolhido[1]])
            matriz_carros = marca_carro_alugado(matriz_carros, id)

    locacao = [nome_cliente, data_locacao, len(carros_escolhidos), carros_escolhidos]

    return locacao


lista_carros = [
    '0 Porsche YBR7544 Rosa Sport 2015',
    '1 Ford XXX1235 Preto Sport 2019',
    '2 Honda GRE5768 Amarelo Familia 2015',
    '3 Toyota ABC5341 Azul Sport 2022'
]


matriz_carros = criar_matriz_carros(lista_carros)
m_locacoes = []

while True:
    opcao = int(input('''\nEscolha uma característica:
    [1] Marca
    [2] Placa
    [3] Cor
    [4] Modelo
    [5] Ano de fabricação\n
    Digite sua opção: '''))

    if opcao == "1":
        locacao = cria_locacao(matriz_carros)
        m_locacoes.append(locacao)
        print("\nLocação criada com sucesso!\n")
    elif opcao == "2":
        for linha in m_locacoes:
            print(linha)
    elif opcao == "3":
        buscar_carro_por_id(matriz_carros, opcao)
    elif opcao == "0":
        print("\nPrograma encerrado.\n")
        break
    else:
        print("\nOpção inválida. Tente novamente.\n")
