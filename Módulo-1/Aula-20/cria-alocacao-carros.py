'''Desenvolva uma função chamada cria_locacao que simule o processo de aluguel de carros. A função 
deve permitir:
Receber como argumento a matriz de carros disponíveis para locação
Solicitar ao usuário o nome do cliente
Solicitar ao usuário a data da locação
Solicitar ao usuário a quantidade de carros que serão alugados
Exibir a lista de carros disponíveis para locação, apresentando as informações de cada carro.
Permitir que o usuário escolha os carros que deseja alugar. O usuário deve informar o ID de cada 
carro desejado.(Utilize a função buscar_carro_por_id e marca_carro_alugado )
Armaze todas as informações em uma lista de locacao
Retornar a locacao após o processo de criação da locação.
Na função principal do programa, utilize um loop para criar múltiplas locações. Crie uma matriz 
vazia chamada matriz_locacoes para armazenar as informações das locações. Em cada iteração do loop,
chame a função cria_locacao para criar uma nova locação e adicione-a à matriz matriz_locacoes. 
Isso permite criar várias locações de forma automatizada, sem a necessidade de repetir o código 
manualmente. Ao final do loop, a matriz matriz_locacoes conterá todas as informações das locações, 
incluindo o nome do cliente, a data da locação, a quantidade de carros alugados, o ID e a marca dos 
carros escolhidos. É Opcional utilizar a função para remover um carro, se ele está sendo alugado.
Dica: Exemplo de como pode ser a função principal
matriz_locacoes = []
for _ in range(2):
  locacao = cria_locacao(matriz_carros)
  matriz_locacoes.append(locacao)
  
Digite o nome do cliente: Jucileu
Digite a data da locação: 20-03
Digite a quantidade de carros a serem alugados: 2
Carros disponíveis para locação:
ID: 0, Marca: Porsche, Placa: YBR7544, Cor: Rosa, Modelo: Sport, Ano: 2015
ID: 1, Marca: Ford, Placa: XXX1235, Cor: Preto, Modelo: Sport, Ano: 2019
ID: 2, Marca: Honda, Placa: GRE5768, Cor: Amarelo, Modelo: Familia, Ano: 2015
ID: 3, Marca: Toyota, Placa: ABC5341, Cor: Azul, Modelo: Sport, Ano: 2022
Digite o ID do 1º carro a ser alugado: -
Digite o ID do 2º carro a ser alugado: 1
#Locação criada com sucesso!

Digite o nome do cliente: João Clesio
Digite a data da locação: 20-03
Digite a quantidade de carros a serem alugados: 2
Carros disponíveis para locação:
ID: 0, Marca: Porsche, Placa: YBR7544, Cor: Rosa, Modelo: Sport, Ano: 2015
ID: 1, Marca: Ford, Placa: XXX1235, Cor: Preto, Modelo: Sport, Ano: 2019
ID: 2, Marca: Honda, Placa: GRE5768, Cor: Amarelo, Modelo: Familia, Ano: 2015
ID: 3, Marca: Toyota, Placa: ABC5341, Cor: Azul, Modelo: Sport, Ano: 2022
Digite o ID do 1º carro a ser alugado: 3
Digite o ID do 2º carro a ser alugado: 2
#Locação criada com sucesso!
Nome do cliente: Jucileu, Data da locação: 20-03, Quantidade de carros: 2, Carros alugados: [['1', 'Ford']]
Nome do cliente: João Clesio, Data da locação: 20-03, Quantidade de carros: 2, Carros alugados: [['3', 'Toyota'], ['2', 'Honda']]'''


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
    qtd_carros = int(input("\nDigite a quantidade de carros que dejeja alugar: "))

    print("\nCarros disponveis para locação:")
    for carro in matriz_carros:
        if len(carro) <= 6:
            print(f"ID: {carro[0]}, Marca: {carro[1]}, Placa: {carro[2]}, Cor: {carro[3]}, Modelo: {carro[4]}, Ano: {carro[5]}")

    carros_escolhidos = []

    for i in range(qtd_carros):
        id = input(f"\nDigite o ID do {i + 1}° carro: ")

        carro_escolhido = buscar_carro_por_id(matriz_carros, id)
        if len(carro_escolhido) > 6 and carro_escolhido[6] == 'Alugado':
            print("\nCarro escolhido já está alugado !\n")
        else:
            carros_escolhidos.append([carro_escolhido[0], carro_escolhido[1]])
            matriz_carros = marca_carro_alugado(matriz_carros, id)

    locacao = [nome_cliente, data_locacao, len(carros_escolhidos), carros_escolhidos]
    return locacao


matriz_carros = [
    ['0', 'Porsche', 'YBR7544', 'Rosa', 'Sport', '2015'],
    ['1', 'Ford', 'XXX1235', 'ROSA', 'Sport', '2019'],
    ['2', 'Honda', 'GRE5768', 'Amarelo', 'Familia', '2015'],
    ['3', 'Toyota', 'ABC5341', 'Azul', 'Sport', '2022']
]

matriz_locacoes = []

for _ in range(2):
    locacao = cria_locacao(matriz_carros)
    matriz_locacoes.append(locacao)
