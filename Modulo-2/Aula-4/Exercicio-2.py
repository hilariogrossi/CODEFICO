'''Imagine que você está projetando um programa para um site de sorteios. O site utiliza tuplas para
armazenar os números adquiridos pelos participantes, porém, a empresa exige no mínimo dois números 
por compra. Você deve criar um programa que armazene todas as tuplas com os números comprados em uma
lista, descartando as tentativas de compra de apenas 1 número. O programa deve receber uma lista de 
tuplas como entrada e retornar uma lista contendo apenas as tuplas que têm um tamanho maior que 1.
Passo 1: Inserir o número de tuplas. Passo 2: Crie um loop para registrar os números nas tuplas.
Passo 3: Dentro do loop criar uma condição para passar para a próxima tupla.
Passo 4: Criar um loop para conferir se as tuplas tem tamanho maior que 1.
Entrada: Digite o numero de apostas: 3
Digite um número ou "/" para terminar a aposta:12
Digite um número ou "/" para terminar a aposta:21
Digite um número ou "/" para terminar a aposta:30
Digite um número ou "/" para terminar a aposta:/
Digite um número ou "/" para terminar a aposta:15
Digite um número ou "/" para terminar a aposta:16
Digite um número ou "/" para terminar a aposta:/
Digite um número ou "/" para terminar a aposta:2
Digite um número ou "/" para terminar a aposta:/
Saída: [('12', '21', '30'), ('15', '16')]'''

quantidade_apostas = int(input('\nDigite o numero de apostas: '))
loop_lista = []

for _ in range(quantidade_apostas):
    loop_tupla = []
    aposta = input('\nDigite um número ou "/" para terminar a aposta: ')

    while aposta != '/':
        loop_tupla.append(aposta)

        aposta = input('\nDigite um número ou "/" para terminar a aposta: ')

    if len(loop_tupla) < 2:
        continue

    loop_lista.append(tuple(loop_tupla))

print(loop_lista)
