'''Crie uma função que liste e imprima na tela pelo menos 6 produtos(enumerados) disponíveis para
venda em uma loja, juntamente com seus respectivos preços. Você tem liberdade para escolher quais
produtos sua loja irá vender e os preços. Dicas: utilize variáveis para armazenar os preços e ao
defini-las, utilize o nome do produto + "_preço" ex.: petisco_preço. Não é necessário armazenar
o nome dos produtos em variáveis. Em seguida, você precisa simular a venda de um desses produtos.
O usuário irá fornecer o número do produto que deseja comprar e a quantidade desejada. A função
deve retornar o valor dessa compra a depender da quantidade solicitada.
Agora, utilizando a questão anterior, crie uma função de loop para que o cliente possa escolher
entre 2 opções: 1-fazer mais compras ou 2-encerrar a compra. Assim, o programa irá perguntar
diversas vezes se ele quer fazer mais compras, até ele escolher encerrar. Ao final, exiba na tela
o valor final que ele deve pagar. Ou seja, a soma de todas as compras feitas. Dica: 1- o valor da
compra se refere apenas à uma compra. Já o valor final é a soma de todas as compras'. 2- Utilize
o comando de loop para que o usuario sempre possa escolher entre encerrar ou fazer mais compras.'''


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


def mais(continuar):
    valor_final = 0

    while continuar == 1:
        valor_final += petShop()

        continuar = int(input('\nDeseja continuar comprando [1] ou Encerrar compra [2]: '))

    return valor_final


valor_total = mais(1)

print(f'\nO valor total da compra foi de R$ {valor_total:.2f}\n')
