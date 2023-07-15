'''Faça uma função chamada TextoParaMatriz que receba uma string contendo uma lista de valores
como inteiros e retorne uma matriz que tem os elementos da lista da entrada, no entanto organizados
em uma lista de lista de inteiros (matriz de inteiros). A string da entrada tem o espaço como
separador de colunas e o ponto e vírgula como separador de linhas.
Ex. 1 2 3; 4 5 6; 7 8 9
Faça o programa principal para testar a função. Observação: Programa 2 da Semana 7 é usado de
referência. (Conceito utilizado: função para transformar texto em matriz)'''

def TextoParaMatriz(texto):
    linhas = texto.split(';')
    matriz = []

    for linha in linhas:
        colunas = linha.split()
        linha_convertida = [int(coluna) for coluna in colunas]
        matriz.append(linha_convertida)

    print('\n')

    for linha in matriz:
        for elemento in linha:
            print(f' {elemento}', end=' ')
        print()

    print('\n')

entrada = input('\nEntre com a matriz em forma de string: ')
TextoParaMatriz(entrada)
