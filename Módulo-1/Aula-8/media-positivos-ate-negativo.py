'''Escreva uma função chamada media_positivos que solicita ao usuário que insira uma série de
números inteiros positivos e calcula a média desses números. A função deve continuar solicitando
números até que o usuário insira um número negativo. Em seguida, a função deve retornar a média
dos números positivos inseridos. Caso nenhum número positivo for inserido, a função deve retornar
"None". A função principal deve imprimir a média caso a entrada seja válida, ou uma mensagem de
erro caso seja inválida Dica: Média = Soma dos números / Quantidade de números'''


def media_positivos():
    soma = quantidade = 0

    print('\nPARA TERMINAR O LAÇO DIGITE UM NÚMERO NEGATIVO!')

    while True:
        numero = int(input('\nEntre com o número: '))

        if numero < 0:
            break
        
        soma += numero
        quantidade += 1

    if quantidade == 0:
        return None
    
    return soma / quantidade


resultado = media_positivos()

if resultado is None:
    print('\nNENHUM NÚMERO POSITIVO FOI DIGITADO!\n')
else:
    print(f'\nA média dos números positivos é: {resultado}.\n')
