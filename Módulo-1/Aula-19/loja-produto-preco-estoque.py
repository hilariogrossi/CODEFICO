'''O Se. Apu Nahasapeemapetilon é proprietário de uma vendedora de acessórios para computador a
Kwik E´ Mart. Esta empresa possui 4 lojas e o Sr. Apu matém um estoque mínimo de produtos em 
todas as lojas: HD (100 unidades): impressora (40 unidades): monitor (50 unidades: notebook (30
unidades): e tablet (80 inidades). Estas informações podem ser representadas eplos vetores:
produto = ['HD', 'impressora', 'monitor', 'notebook', 'tablet']
minino = [100, 40, 50, 30, 80]
Conforme apresentado nesses vetores vemos que a quantidade mínima de HD´s é 100 e a quantidade 
mínima de notebook é 30. Os estoques das 4 lojas são representados por uma matriz (estoque), onde
cada linha representa o estoque de uma determinada loja. Seja a seguinte matriz estoque:
|41     48      32      32      81  | estoque loja 1
|102    38      40      15      85  | estoque loja 2
|100    40      50      30      80  | estoque loja 3
|100    40      50      35      78  | estoque loja 4
Considere um program no qual os vetores produto e mínimo, assim como a matriz estoque, já foram
lidos no início do programa. No caso basta declar os vetores e a matriz no início do programa.
Escreva o restante do código desse programa.'''

produto = ["HD", "Impressora", "Monitor", "Notebook", "Tablet"]
minimo = [100, 40, 50, 30, 80]
estoque = [
    [41, 48, 32, 32, 81], #  estoque loja 1
    [102, 38, 50, 15, 85], #  estoque loja 2
    [100, 40, 50, 30, 80], #  estoque loja 3
    [100, 40, 50, 35, 78] #  estoque loja 4
]

print('\nRELATÓRIO DO ESTOQUE:')

for loja, estoque_loja in enumerate(estoque):
    print(f'\nLoja Número {loja + 1}\n')

    produtos_em_falta = []

    for produto_indice, quantidade in enumerate(estoque_loja):
        if quantidade < minimo[produto_indice]:
            falta = minimo[produto_indice] - quantidade
            produtos_em_falta.append(f'{produto[produto_indice]} - Faltam {falta} unidades.')

    if produtos_em_falta:
        for produto_em_falta in produtos_em_falta:
            print(produto_em_falta)
    else:
        print('Todos os produtos possuem o estoque mínimo!')

print('\n')
