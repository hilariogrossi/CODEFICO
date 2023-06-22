# Classificação de Vendas por Idade em uma Mercearia
# Você foi contratado para desenvolver um programa para uma mercearia que possui algumas restrições
# de venda de acordo com a idade do cliente. A mercearia vende 6 produtos: 1-Vidro, 2-Fósforo,
# 3-Refrigerante, 4-Chocolate, 5-Alcool. O programa deve solicitar o nome, idade do cliente e o
# numero do produto que ele quer comprar. Se o cliente tiver menos de 18 anos, os produtos 1, 2 e 5
# não podem ser vendidos. Se o cliente tiver menos de 18 anos e se chamar "Jubiscleisson", ele não
# pode comprar Refrigerante. Se o cliente tiver mais de 18 anos, ele poderá comprar qualquer item
# da loja. O programa deve exibir uma mensagem informando se o cliente pode ou não comprar o
# produto selecionado, de acordo com as restrições mencionadas.

nome = input('Entre com o seu nome: ')
idade = int(input('Entre com a sua idade: '))

print('\n[1] Vidro, [2] Fósforo, [3] Refrigerante, [4] Chocolate e [5] Álcool\n')

produto = int(input('Entre com o produto desejado: '))

if produto < 1 or produto > 5:
    print('\nNão existe esse produto.\n')
elif produto == 4:
    print(f'\n{nome}, você pode comprar o produto {produto}.\n')
else:
    if idade < 18:
        if (produto == 1 or produto == 2 or produto == 5):
            print(f'\n{nome}, você NÃO pode comprar o produto {produto}.\n')
        elif nome == 'Jubiscleisson' and produto == 3:
            print(f'\n{nome}, você NÃO pode comprar o produto {produto}.\n')
        else:
          print(f'\n{nome}, você pode comprar o produto {produto}.\n')  
    else:
        print(f'\n{nome}, você pode comprar o produto {produto}.\n')
