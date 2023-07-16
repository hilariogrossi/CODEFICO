'''Num jogo de Batalha Naval o oceano pode ser representado por uma matriz de duas dimensões na
qual cada posição de índice (x, y) contem informação sobre o tipo de navio localizado nesta posição
do  oceano: 1 representa um Couraçado; 2 representa um Contratorpedo; 3 representa uma Fragata e 
0 indica que não existe navio na posição. Por exemplo,  no oceano representado pela matriz M abaixo
exitem 2 Couraçados, nas posições (3, 4) e (5, 8); 3 Contratorpedos nas posições (5, 3) e (5, 6) e
(6, 1) e também 2 Fragatas nas posições (1, 2) e (5, 5). No nosso jogo de Batalha Naval um jogador 
tenta acertar posições de navios no oceano dando n palpites das posições (x, y). Caso exista um 
navio numa posição informada ele soma pontos conforme o tipo de navio existente, de acordo com a
seguinte    tabela
             Número ==> Navio ==>       Pontos
               1        Coraçado          20
               2        Contratorpedo     30
               3        Fragata           10
Escreva um programa para a Batalha Naval'''

M = [
    [0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 3, 2, 0, 1],
    [2, 3, 0, 0, 0, 0, 0, 0],
    ]

print('\nBATALHA NAVAL\n')

soma_pontos = 0
n = int(input('Digite o número de jogadas: '))

for i in range(n):
    print(f'\n{i + 1}ª jogada:')

    x = int(input('\n   Digite a posição X: '))
    y = int(input('\n   Digite a posição Y: '))

    x -= 1
    y -= 1

    if M[x][y] == 1:
        soma_pontos += 20
    elif M[x][y] == 2:
        soma_pontos += 30
    elif M[x][y] == 3:
        soma_pontos += 10

print(f'\nPontuação obtida: {soma_pontos} pontos.\n')
