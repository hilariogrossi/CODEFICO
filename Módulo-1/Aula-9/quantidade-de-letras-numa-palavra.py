'''Você foi contratado para desenvolver um programa que verifique se uma palavra digitada pelo
usuário tem uma quantidade de letras que seja divisível por 6. Para isso, você precisa implementar
duas funções: A função verificar_tamanho_palavra(palavra) que recebe uma palavra como entrada e
verifica se a quantidade de caracteres que ela possui, é um número divisível por 6. Caso seja,
deve exibir uma mensagem que informa se o número de caracteres é divisível por 6 ou não. A função
programa_tamanho_palavra() que é a função principal do programa, solicita ao usuário que digite uma
palavra e chama a função verificar_tamanho_palavra() para verificar o tamanho da palavra digitada.
Dica: Utilize a função len() para obter o número de caracteres da palavra.'''


def verificar_tamanho_palavra(palavra):
    if len(palavra) % 6 == 0:
        print(f'\nA quantidade de caracteres da palavra "{palavra}" é divisível por 6!\n')
    else:
        print(f'\nA quantidade de caracteres da palavra "{palavra}" NÃO é divisível por 6!\n')


def programa_tamanho_palavra():
    print('\n***PROGRAMA QUE DESCOBRE SE A PALAVRA DIGITADA TEM CARACTERES DIVISÍVEIS POR 6***')

    palavra = input('\nDigite uma palavra: ')

    verificar_tamanho_palavra(palavra)


programa_tamanho_palavra()
