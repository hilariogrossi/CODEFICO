'''Escreva um programa em Python que solicite ao usuário que digite uma sequência de palavras. 
O programa deve armazenar as palavras em uma lista até que o usuário digite a palavra "fim". 
Em seguida, o programa deve exibir na tela a frase digitada pelo usuário, excluindo a palavra
"fim". Dica: Utilize While.'''

sequencia_palavras = []
palavras = input('\nEntre com as palavras: [palavra por palavra][Digite "fim" para encerrar]: ')

while palavras != 'fim':
    sequencia_palavras.append(palavras)
    palavras = input('\nEntre com as palavras: [palavra por palavra][Digite "fim" para encerrar]: ')

print(f'\nA frase digitada é: {" ".join(sequencia_palavras)}.\n')
