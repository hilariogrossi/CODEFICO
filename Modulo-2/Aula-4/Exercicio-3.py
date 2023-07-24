'''Uma loja precisa de um programa que receba o número de vendas de cada dia separadamente e mostre 
o total de vendas de todos os dias inseridos. Crie um programa que receba uma tupla de números 
inteiros como argumento e retorne a soma de todos os elementos da tupla.
Passo 1: Inserir o número de dias. Passo 2: Crie um loop para registrar as vendas de cada dia na 
tupla. Passo 3: Criar um loop para somar os elementos.
Entrada: Digite o numero de dias: 3
Digite o número de vendas do dia 1: 3
Digite o número de vendas do dia 2: 6
Digite o número de vendas do dia 3: 8
Saída: Total: 17'''

quantidade_dias = int(input('\nEntre com a quantidade de dias a ser analisado: '))
lista = []

for i in range(quantidade_dias):
    vendas = float(input(f'\nEntre com a quantidade de venda do {i + 1}° dia: '))
    lista.append(vendas)

tupla = tuple(lista)
soma = 0

for i, elemento in enumerate(tupla):
    soma += elemento

print(f'\nA soma de todos os elementos da tupla {tupla} é R$ {soma:.2f}\n')
