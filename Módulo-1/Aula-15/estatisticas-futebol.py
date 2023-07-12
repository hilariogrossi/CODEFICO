'''Estatística de futebol'''


def calcular_estatisticas():
    nome_juiz = input('\nDigite o nome do juiz: ')

    quantidade_partidas = int(input('\nInforme a quantidade de partidas: '))

    total_impedimentos = total_faltas = total_cartoes = total_acrescimo = 0

    for i in range(quantidade_partidas):
        impedimentos = int(input(f'\nPartida({i + 1}) - Informe os impedimentos: '))
        faltas = int(input(f'\nPartida({i + 1}) - Informe as faltas: '))
        cartoes = int(input(f'\nPartida({i + 1}) - Informe os cartões: '))
        tempo = float(input(f'\nPartida({i + 1}) - Informe o tempo de acréscimo: '))

        print()

        total_impedimentos += impedimentos
        total_faltas += faltas
        total_cartoes += cartoes
        total_acrescimo += tempo

    media_impedimentos = total_impedimentos / quantidade_partidas
    media_faltas = total_faltas / quantidade_partidas
    media_cartoes = total_cartoes / quantidade_partidas
    media_tempo = total_acrescimo / quantidade_partidas

    print(f'\nEstatísticas do juiz {nome_juiz}\n')
    print(f'\nMédia de impedimentos: {media_impedimentos:.2f}')
    print(f'\nMédia de faltas: {media_faltas:.2f}')
    print(f'\nMédia de cartões: {media_cartoes:.2f}')
    print(f'\nMédia de acréscimentos: {media_tempo:.2f}\n')


calcular_estatisticas()
