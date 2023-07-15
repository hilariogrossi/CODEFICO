'''Uma imagem em preto e branco pode ser armazenada num computador na forma de uma matriz, onde 0
representa a cor preta e 1 representa a cor branca. Por exemplo, a matriz a seguir representa a 
imagem, em preto e branco, de um triângulo.
                    0001000
                    0010100
                    0100010
                    1111111
                    entrada = 0 0 0 1 0 0 0; 0 0 1 0 1 0 0; 0 1 0 0 0 1 0; 1 1 1 1 1 1 1
Escreva um programa que leia uma matriz que represente uma imagem em preto e branco e inverta as
cores na imagem, isto é, troque cada 0 por 1 e cada 1 por 0. Por exemplo, se a matriz lida como
entrada for a matriz acima o resultado impresso pelo programa deverá ser a seguinte matriz:
                    1110111
                    1101011
                    1011101
                    0000000'''

entrada = input('\nDigite uma matriz imagem: ')
linhas = entrada.split(';')
matriz = []

for linha in linhas:
    colunas = linha.split()
    linha_convertida = [int(coluna) for coluna in colunas]
    matriz.append(linha_convertida)

print('\nImagem com cores invertidas:\n')

for linha in matriz:
    for coluna in linha:
        if linha[coluna] == 0:
            linha[coluna] = 1
        else:
            linha[coluna] = 0

for linha in matriz:
    for elemento in linha:
        print(f'   {elemento}', end=' ')
    print()

print('\n')
