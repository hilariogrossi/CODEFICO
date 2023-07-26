'''Você é responsável por desenvolver um sistema de gerenciamento para uma academia. O sistema deve 
armazenar as informações dos membros em tuplas, contendo nome, idade, peso e altura. Além disso, o 
sistema deverá disponibilizar funcionalidades para exibir as pessoas com mais de 60 anos, calcular o
Índice de Massa Corporal (IMC) de todos os membros, calcular a média de altura dos membros, exibir a
pessoa mais leve e exibir o maior IMC.
Passo 1: Definir a Estrutura de Dados
Crie uma lista vazia para armazenar as tuplas dos membros. Cada tupla conterá as informações de nome,
idade, peso e altura do membro.
Passo 2: Implementar a Função de Cadastro de Novos Membros
Crie uma função chamada cadastrar_membro que recebe o número de membros a serem cadastrados. Dentro 
da função, crie uma tupla que irá receber dados dos novos membros (nome, idade, peso e altura) como 
parâmetros. Depois crie uma lista para receber as tuplas com os membros. Faça um loop a partir do 
número de membros para ler os dados dos membros como input e adicioná-los a lista um por um.
Exiba uma mensagem confirmando o cadastro dos membros. A função deve retornar a lista de membros.
Passo 3: Implementar a Função de Exibição de Pessoas com Mais de 60 Anos
Crie uma função chamada exibir_membros_mais_de_60_anos que receba a lista de membros. Percorra a 
lista de membros e verifique a idade de cada membro. Se a idade do membro for maior que 60 anos exiba
o nome do membro.
Passo 4: Implementar a Função de Cálculo da Média de Altura
Crie uma função chamada calcular_media_altura que receba a lista de membros. A função deve calcular 
a média de altura de todos os membros. Percorra a lista de membros e some as alturas de todos os 
membros. Divida a soma total das alturas pelo número de membros para obter a média. Exiba a média de
altura.
Passo 5: Implementar a Função de Exibição da Pessoa Mais Leve
Crie uma função chamada exibir_pessoa_mais_leve que recebe a lista de membros. Percorra a lista de 
membros e encontre o membro com o menor peso. Exiba o nome e o peso do membro mais leve.
Passo 6: Implementar a Função de Cálculo do IMC de Todos os Membros
Crie uma função chamada calcular_imc que recebe a lista de membros. A função deve calcular o IMC de 
cada membro. Fórmula do IMC = Peso/(Altura x Altura). Percorra a lista de membros e, para cada 
membro, calcule o IMC utilizando a fórmula fornecida. Crie uma lista para armazenar tuplas com o 
nome e IMC de cada membro. Retorne essa lista.
Passo 7: Implementar a Função de Exibição do maior IMC
Crie uma função chamada exibir_maior_IMC que recebe a lista de IMCs retornada acima. Percorra a 
lista de IMC e encontre o membro com o maior IMC. Exiba o nome e o IMC da pessoa.
Passo 8: Implementar um Menu
Crie um loop para que o menu continue sendo exibido após o usuário selecionar uma opção até que ele 
decida sair. Com base na escolha do usuário, chame a função correspondente à opção selecionada ou 
execute o código necessário. (Crie uma opção para sair do loop) Lembre-se de imprimir as opções a 
cada loop do menu. Use seus conhecimentos e criatividade para desenvolver o layout e funcionalidades
do menu!
Exemplo 1: Entrada: Digite 1: para cadastrar membros; Digite 2: para exibir as pessoas com mais de 
60 anos; Digite 3: para calcular a média de altura geral; Digite 4: para exibir a pessoa mais leve;
Digite 5: para exibir os IMCs; Digite 6: para exibir o maior IMC da academia; Digite 0: para SAIR;
Digite: 1
Digite o número de membros que deseja inserir: 3
Digite o nome:Davi Digite a idade:20 Digite o peso:67 Digite a altura:1.74
Digite o nome:Roger Digite a idade:66 Digite o peso:75 Digite a altura:1.78
Digite o nome:Leticia Digite a idade:33 Digite o peso:63 Digite a altura:1.7
Saída: A função apenas realiza a inserção dos membros na lista e retorna essa lista.

Exemplo 2: Entrada: Digite 1: para cadastrar membros; Digite 2: para exibir as pessoas com mais de 
60 anos; Digite 3: para calcular a média de altura geral; Digite 4: para exibir a pessoa mais leve;
Digite 5: para exibir os IMCs; Digite 6: para exibir o maior IMC da academia; Digite 0: para SAIR;
Digite: 2
Saída: Membros idosos: Roger

Exemplo 3: Entrada: Digite 1: para cadastrar membros; Digite 2: para exibir as pessoas com mais de 
60 anos; Digite 3: para calcular a média de altura geral; Digite 4: para exibir a pessoa mais leve;
Digite 5: para exibir os IMCs; Digite 6: para exibir o maior IMC da academia; Digite 0: para SAIR;
Digite: 3
Saída: Média geral de altura: 1.74

Exemplo 4: Entrada: Digite 1: para cadastrar membros; Digite 2: para exibir as pessoas com mais de 
60 anos; Digite 3: para calcular a média de altura geral; Digite 4: para exibir a pessoa mais leve;
Digite 5: para exibir os IMCs; Digite 6: para exibir o maior IMC da academia; Digite 0: para SAIR;
Digite: 4
Saída: Membro mais leve: Leticia

Exemplo 5: Entrada: Digite 1: para cadastrar membros; Digite 2: para exibir as pessoas com mais de 
60 anos; Digite 3: para calcular a média de altura geral; Digite 4: para exibir a pessoa mais leve;
Digite 5: para exibir os IMCs; Digite 6: para exibir o maior IMC da academia; Digite 0: para SAIR;
Digite: 5
Saída: IMC dos membros: Nome: Davi - IMC: 22.13 Nome: Roger - IMC: 23.67 Nome: Leticia - IMC: 21.80

Exemplo 6: Entrada: Digite 1: para cadastrar membros; Digite 2: para exibir as pessoas com mais de 
60 anos; Digite 3: para calcular a média de altura geral; Digite 4: para exibir a pessoa mais leve;
Digite 5: para exibir os IMCs; Digite 6: para exibir o maior IMC da academia; Digite 0: para SAIR;
Digite: 6
Saída: Membro com maior IMC: Roger'''

membros = []


def cadastrar_membro(n1):
    for i in range(n1):
        tupla_membro = []

        nome = input(f'\nDigite o {i + 1}° nome: ')
        tupla_membro.append(nome)

        idade = int(input(f'\nDigite a {i + 1}ª idade: '))
        tupla_membro.append(idade)

        peso = float(input(f'\nDigite o {i + 1}° peso: '))
        tupla_membro.append(peso)

        altura = float(input(f'\nDigite a {i + 1}ª altura: '))
        tupla_membro.append(altura)

        membros.append(tuple(tupla_membro))

    print('\nCadastro do(s) membro(s) efetuado com sucesso!\n')

    return membros


def exibir_membros_mais_de_60_anos(membros):
    nome_maior_60 = ''
    for i in range(len(membros)):
        if membros[i][1] > 60:
            nome_maior_60 = membros[i][0]
    print(f'A(s) pessoa(s) que tem mais de 60 anos é/são: {nome_maior_60}')


def calcular_media_altura(membros):
    soma = media = 0
    for i in range(len(membros)):
        soma += membros[i][3]

    media = soma / len(membros)

    print(f'\nA média das alturas é {media}\n')


def exibir_pessoa_mais_leve(membros):
    peso = float('inf')
    pessoa_mais_leve = ''
    for i in range(len(membros)):
        if membros[i][2] < peso:
            peso = membros[i][2]
            pessoa_mais_leve = membros[i][0]

    print(f'\nA pessoa mais leve é: {pessoa_mais_leve}, com o peso: {peso:.2f}\n')


def calcular_imc(membros):
    lista_imc = []

    for n in range(len(membros)):
        imc = membros[n][2]/(membros[n][3] ** 2)
        tup_imc = membros[n][0], imc
        lista_imc.append(tup_imc)

    return lista_imc


def exibir_maior_IMC(IMC):
    maior_IMC = float('-inf')
    nome_maior_IMC = ''
    for i in range(len(IMC)):
        if IMC[i][1] > maior_IMC:
            maior_IMC = IMC[i][1]
            nome_maior_IMC = IMC[i][0]

    print(f'O membro com maior IMC é: {nome_maior_IMC} e o IMC é: {maior_IMC:.2f}')


lista_membros = []

while True:
    lista_IMC = calcular_imc(lista_membros)

    opcao = int(input('''
        Digite 1: Cadastrar membros;
        Digite 2: Exibir as pessoas com mais de 60 anos;
        Digite 3: Calcular a média de altura geral;
        Digite 4: Exibir a pessoa mais leve;
        Digite 5: Exibir os IMCs;
        Digite 6: Exibir o maior IMC da academia;
        Digite 0: SAIR;

        Sua opção: '''))
    
    print()

    if opcao == 1:
        numero_membro = int(input('\nDigite o número de membros que deseja inserir: '))
        lista_membros += cadastrar_membro(numero_membro)
    elif opcao == 2:
        exibir_membros_mais_de_60_anos(lista_membros)
    elif opcao == 3:
        calcular_media_altura(lista_membros)
    elif opcao == 4:
        exibir_pessoa_mais_leve(lista_membros)
    elif opcao == 5:
        for i in range(len(lista_IMC)):
            print(f'\nNome : {lista_IMC[i][0]} e IMC: {lista_IMC[i][1]:.2f}\n')
    elif opcao == 6:
        exibir_maior_IMC(lista_IMC)
    elif opcao == 0:
        print('\nSAINDO DO PROGRAMA... Obrigado por utilizar o Hilário´s program!\n')
        break
    else:
        print('\nOPÇÃO INVÁLIDA. Tente novamente...\n')
