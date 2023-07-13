'''A administração do RU da UFOP fez uma pesquisa sobre a qualidade das refeições.
Vários alunos responderam a pesquisa com números de 1 a 5, que representam uma escala
de satisfação, a saber: 1 – péssima; 2 – ruim; 3 – boa; 4 – muito boa; e 5 – excelente.
As respostas dadas pelos alunos que participaram da pesquisa estão armazenadas em um
vetor respostas, tal como o mostrado a seguir:
respostas = [1, 2, 5, 4, 2, 1, 5, 4, 1, 2, 5, 3, 2, 1, 2, 4, 2, 3, 5, 1, 4, 1, 2, 4, 5, 5, 1, 2,
3, 4, 3, 4, 2, 1, 5, 1, 2, 4, 5, 3, 1, 2, 5, 4, 1, 1, 2, 5, 4, 3]
Escreva o código do programa, de modo que o programa gere um vetor contendo o número de
vezes que ocorreu cada resposta. Ou seja, esse vetor deve conter, em cada posição i,
para 1<=i<=5, o número de vezes que ocorreu a resposta i. O programa deve imprimir a
frequência de cada resposta (1 a 5) em formato de um registro por linha.
(Conceito utilizado: nova lista com resultado de votação)'''

respostas = [1, 2, 5, 4, 2, 1, 5, 4, 1, 2, 5, 3, 2, 1, 2, 4, 2, 3, 5, 1, 4, 1, 2, 4, 5, 5, 1, 2, 3, 4, 3, 4, 2, 1, 5, 1, 2, 4, 5, 3, 1, 2, 5, 4, 1, 1, 2, 5, 4, 3]
resultado = [0, 0, 0, 0, 0, 0]

for i in range(len(respostas)):
    resultado[respostas[i]] += 1

print('''Graus de satisfação:
    1 - péssima;
    2 - ruim;
    3 - boa;
    4 - muito boa e
    5 - excelente\n''')

for i in range(1, len(resultado)):
    print(f'Satisfação {i}: {resultado[i]} votos.', end=' | ')

print('\n')
