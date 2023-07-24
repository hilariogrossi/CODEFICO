'''Um banco adotou uma política de prioridade que realiza o atendimento começando pela pessoa mais 
velha na sala de espera. Eles precisam de um programa que mostre quem será a próxima pessoa a ser 
atendida. Escreva um programa que receba uma lista de tuplas, onde cada tupla contém o nome e a 
idade de uma pessoa. A função deve retornar o nome da pessoa mais velha.
Passo 1: Inserir o número pessoas. Passo 2: Crie um loop para registrar o nome e idade da pessoa em 
uma tupla. Passo 3: Criar um loop comparar e armazenar a pessoa mais velha.
Entrada: Digite o numero de pessoas: 3
Digite o nome:Davi - Digite a idade:20
Digite o nome:Messias - Digite a idade:19
Digite o nome:Lucas - Digite a idade:18
Saída: Pessoa mais velha: Davi'''

pessoas = int(input('\nEntre com o número de pessoas: '))
lista = []

for _ in range(pessoas):
    tupla = []
    nome = input('\nEntre com o nome da pessoa: ')
    tupla.append(nome)

    idade = int(input('\nEntre com a idade dessa pessoa: '))
    tupla.append(idade)

    lista.append(tuple(tupla))

idade_maxima = -1
nome_pessoa_idosa = ''

for n in range(pessoas):
    if lista[n][1] > idade_maxima:
        idade_maxima = lista[n][1]
        nome_pessoa_idosa = lista[n][0]

print(f'\nO nome da próxima pessoa a ser atendida é o(a) {nome_pessoa_idosa}\n')
