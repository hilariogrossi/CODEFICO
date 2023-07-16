'''Dispulta entre Cruzeiro e Atlético. Quem ganha?'''

# 2 1; 2 3; 2 0; 0 1; 1 1; 2 3
# 2 0; 1 1; 2 2; 0 1; 0 0

entrada = input('\nTABELA DE RESULTADOS DE JOGOS: ')
linhas = entrada.split(';')
matriz = []

for linha in linhas:
    colunas = linha.split()
    linha_modificada = [int(coluna) for coluna in colunas]
    matriz.append(linha_modificada)

cont_atletico = cont_cruzeiro = empate = 0

for linha in matriz:
    if linha[0] > linha[1]:
        cont_atletico += 1
    elif linha[1] > linha[0]:
        cont_cruzeiro += 1
    else:
        empate += 1

print(f'\nVITÓRIAS DO ATLÉTICO = {cont_atletico}')
print(f'\nVITÓRIAS DO CRUZEIRO = {cont_cruzeiro}')
print(f'\nEMPATES = {empate}')

if cont_atletico > cont_cruzeiro:
    print('\nATLÉTICO É O MELHOR TIME!\n')
elif cont_atletico < cont_cruzeiro:
    print('\nCRUZEIRO É O MELHOR TIME!\n')
else:
    print('\nOS TIMES MAIS EMPATARAM DO QUE VENCERAM UM A OUTRO.\n')
