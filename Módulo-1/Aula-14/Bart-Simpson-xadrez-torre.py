'''Bart Simpson está aprendendo a jogar xadrez e tem dificuldade em saber para qual direção
ele pode mover sua Torre. Sabemos que um tabuleiro de xadrez é composto por 8 linhas e 8
colunas, e que a Torre se move ortogonalmente, ou seja, pelas linhas (horizontais) e pelas
colunas (verticais).
Escreva um programa que solicite ao Bart a entrada do número da linha e da coluna que indicam
a posição de sua Torre (ambos inteiros). O programa imprime quais são os possíveis movimentos
da Torre. Utilize o valor 0 para indicar uma casa do tabuleiro para a qual a Torre não pode
ser movida e o valor 1 para indicar uma casa para a qual ela pode ser movida.
Caso a linha ou a coluna não esteja no intervalo de números válidos, [1, 8], a mensagem
“Entrada inválida” deve ser impressa na tela e o programa deve solicitar um novo valor.'''

linha = int(input('\nEntre com a posição da linha no tabuleiro: [1, 8] '))

while linha < 1 or linha > 8:
    print('\nENTRADA INVÁLIDA!')
    linha = int(input('\nEntre com a posição da linha no tabuleiro: [1, 8] '))

coluna = int(input('\nEntre com a posição da coluna no tabuleiro: [1, 8] '))

while coluna < 1 or coluna > 8:
    print('\nENTRADA INVÁLIDA!')
    coluna = int(input('\nEntre com a posição da coluna no tabuleiro: [1, 8] '))

print()
print('    1 2 3 4 5 6 7 8 ')
print('------------------- ')

for i in range(1, 9):
    print(f'{i}', end=' | ')

    for j in range(1, 9):
        if i == linha or j == coluna:
            print('1', end=' ')
        else:
            print('0', end=' ')

    print(' ')

print(' ')
