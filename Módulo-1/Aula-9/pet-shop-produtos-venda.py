'''Crie uma função que liste e imprima na tela pelo menos 6 produtos(enumerados) disponíveis para
venda em uma loja, juntamente com seus respectivos preços. Você tem liberdade para escolher quais
produtos sua loja irá vender e os preços. Dicas: utilize variáveis para armazenar os preços e ao
defini-las, utilize o nome do produto + "_preço" ex.: petisco_preço. Não é necessário armazenar
o nome dos produtos em variáveis. Em seguida, você precisa simular a venda de um desses produtos.
O usuário irá fornecer o número do produto que deseja comprar e a quantidade desejada. A função
deve retornar o valor dessa compra a depender da quantidade solicitada.'''


def petShop():
    print('\nProdutos disponíveis na loja Pet&Pet:')
    print('''
    [1] Coleira de Gato
    [2] Coleira de Cachorro
    [3] Ração de Gato 10kg
    [4] Ração de Cachorro 10kg
    [5] Whiskas para gatos
    [6] Petiscos''')

    produto = int(input('\nEscolha seu produto: '))

    if produto == 1:
        preco = 25
    elif produto == 2:
        preco = 30
    elif produto == 3:
        preco = 80.35
    elif produto == 4:
        preco = 85.15
    elif produto == 5:
        preco = 13.10
    elif produto == 6:
        preco = 10.30
    else:
        print('\nPRODUTO NÃO EXITE! Tente novamente...\n')
        exit()

    quantidade = int(input('\nQual a quantidade desse produto deseja: '))

    return preco * quantidade


print(f'\nO valor da compra final foi de R$ {petShop():.2f}\n')
