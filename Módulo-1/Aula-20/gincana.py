'''GINCANA. Quem vence?'''
# gincana = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1], [0, 1, 0, 1, 1, 1, 0, 0, 1, 0], [1, 1, 1, 0, 0, 0, 1, 1, 0, 0]]

pontuacao = [ 10, 7, 20, 5, 12, 30, 9, 10, 15, 30 ]

entrada = input('\nTarefas realizadas por equipe: ')
linhas = entrada.split(';')
matriz_principal = []

for linha in linhas:
    colunas = linha.split()
    linha_convertida = [int(coluna) for coluna in colunas]
    matriz_principal.append(linha_convertida)

print('\n Equipe   Pontos:\n')

maior = -1

for linha in range(len(matriz_principal)):
    soma_equipe = sum(matriz_principal[linha][coluna] *
                       pontuacao[coluna] for coluna in range(len(matriz_principal[linha])))
    print(f'    {linha + 1}     {soma_equipe:4d}')

    if soma_equipe > maior:
        maior = soma_equipe
        vencedora = linha + 1

print(f'\nA equipe {vencedora} é a vencedora.\n')
