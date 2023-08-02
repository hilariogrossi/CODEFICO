'''Desenvolva um programa em Python para gerenciar uma lista de contatos em um arquivo de texto. 
O programa deve fornecer um menu de opções para permitir ao usuário adicionar novos contatos, 
excluir contatos existentes e exibir a lista de contatos atualizada. Ao iniciar o programa, a lista 
de contatos será carregada a partir do arquivo "contatos.txt" (caso o arquivo exista). O programa 
exibirá um menu de opções para o usuário interagir e escolher as seguintes ações:
- Adicionar contato: O programa solicitará ao usuário que digite o nome e o número do contato a ser 
adicionado. Em seguida, o contato será adicionado à lista e gravado no arquivo.
- Excluir contato: O programa exibirá a lista de contatos atual e solicitará ao usuário que digite o
número do contato a ser excluído. Em seguida, o contato será removido da lista e a lista atualizada 
será gravada no arquivo.
- Exibir contatos: O programa exibirá a lista de contatos atual, numerados sequencialmente.
- Sair: O programa será encerrado.
Após a execução de cada ação (exceto sair), o programa deve exibir uma mensagem de confirmação 
adequada. Exemplo de Execução:
Suponha que o arquivo "contatos.txt" já exista e contenha os seguintes contatos:
Pedro: 123456789
Maria: 987654321
Ao iniciar o programa, ele exibirá o seguinte menu:
====== Menu Geral ======
    [1] - Adicionar Contato
    [2] - Excluir Contato
    [3] - Listar Contato
    [4] - Sair
===========================

Escolha uma opção:

Suponha que o usuário escolha a opção 1 para adicionar um novo contato:
Escolha uma opção: 1

Digite o nome do contato: João
Digite o número do contato: 555555555

Contato adicionado com sucesso!

Em seguida, se o usuário escolher a opção 3 para exibir os contatos:
Escolha uma opção: 3

Lista de Contatos:
1. Pedro: 123456789
2. Maria: 987654321
3. João: 555555555
Escolha uma opção: 2

Digite o número do contato a ser excluído: 2

Contato excluído com sucesso!

E, por fim, se o usuário escolher a opção 4 para sair:
Escolha uma opção: 4

Programa encerrado.

Após o encerramento do programa, o arquivo "contatos.txt" será atualizado com as alterações 
realizadas pelo usuário. Espera-se que o programa permita ao usuário adicionar, excluir e exibir 
contatos em um arquivo de gerenciamento de contatos, fornecendo uma interface intuitiva e funcional.
Boa sorte na implementação do programa!'''


def menu():
    while True:
        opcao = int(input('''\n
        ========= Menu Geral =========
            [1] - Adicionar Contato
            [2] - Excluir Contato
            [3] - Listar Contato
            [4] - Sair
        ==============================

        Escolha uma opção: '''))

        if opcao == 1:
            nome = input('\nDigite o nome do contato: ')
            numero = input('\nDigite o número do contato: ')
            adicionar_contato(nome, numero)

        elif opcao == 2:
            n = input('\nDigite o número do contato a ser excluído: ')
            excluir_contato(n)

        elif opcao == 3:
            listar_contatos()

        elif opcao == 4:
            print('\nEncerrando o programa...\n')
            break

        else:
            print('\nOPÇÃO INVÁLIDA Tente novamente...\n')


def adicionar_contato(nome, numero):
    with open('Aula-3/contatos.txt', 'a') as arquivo:
        arquivo.write(nome + ':' + numero + '\n')

    print('\nContato adicionado com sucesso!\n')


def excluir_contato(n):
    with open('Aula-3/contatos.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    with open('Aula-3/contatos.txt', 'w') as arquivo:
        for i, elemento in enumerate(linhas):
            if (i + 1) != n:
                arquivo.write(elemento)

    print("\nContato excluido com sucesso\n")


def listar_contatos():
    with open('Aula-3/contatos.txt', 'r') as arquivo:
        contatos = arquivo.readlines()

    if contatos:
        print('\n==========LISTA CONTATOS==========\n')

        for i, elemento in enumerate(contatos):
            print(f'{i + 1}: {elemento}')

        print('==================================')

    else:
        print('\nNÃO HÁ CONTATOS!\n')


menu()
