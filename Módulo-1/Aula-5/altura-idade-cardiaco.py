# Um parque de diversões oferece um desconto especial em determinadas condições para a entrada
# no brinquedo "Montanha-Russa Extrema". Para ter direito ao desconto, o usuário deve satisfazer
# todas as seguintes condições:
# Ter altura igual ou superior a 1,40 metros.
# Ter idade entre 12 e 60 anos (inclusive).
# Não possuir problemas cardíacos.
# Escreva um programa que solicita ao usuário sua altura, idade e uma resposta ('s' ou 'n')
# indicando se possui problemas cardíacos. O programa deve utilizar os operadores lógicos adequados
# para verificar se o usuário atende a todas as condições e, em caso afirmativo, exibir a mensagem
# "Você tem direito ao desconto na Montanha-Russa Extrema!". Caso contrário, exiba a mensagem
# "Você não atende aos requisitos para o desconto na Montanha-Russa Extrema."

cardiaco = input('\nVocê é cardíaco? [S] ou [N]: ').upper()

if cardiaco == 'S':
    print('\nVocê não atende aos requisitos para o desconto na Montanha-Russa Extrema.\n')
elif cardiaco == 'N':
    altura = float(input('\nEntre com o valor de sua altura em metros: '))
    idade = int(input('\nEntre com a sua idade em anos: '))

    if altura >= 1.4 and 12 <= idade <= 60:
        print('\nVocê tem direito ao desconto na Montanha-Russa Extrema!\n')
    else:
        print('\nVocê não atende aos requisitos para o desconto na Montanha-Russa Extrema.\n')
else:
    print('\nVOCÊ DIGITOU A SUA CONDIÇÃO CARDÍACA ERRADA. Encerrando o programa...\n')
