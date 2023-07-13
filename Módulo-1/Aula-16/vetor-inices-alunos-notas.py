'''Considere dois vetores já armazenados na memória do computador. Um vetor com os nomes
dos alunos e outro com as notas semestrais de BCC701 desses alunos. Uma forma de ilustrar
esses vetores é apresentada a seguir:
nome = [“Skywalker”, “Kenobi”, “Solo”, “Vader”, “Organa”, “Amidala”, “Finn”, “Rey” ]
nota = [5.8, 10.0, 8.5, 4.5, 3.2, 6.5, 3.5, 6.4]
Escreva um programa que:
1) Gere um vetor de índices, Index. Este vetor contém as posições dos elementos do vetor
nota cujos valores são maiores ou iguais a 6.0 (critério de aprovação);
2) Utilizando o vetor Index (ou seja, sem utilizar o vetor nota nesse ponto), o programa
imprime o nome dos alunos que foram aprovados (a partir do vetor nome).
A seguir o vetor Index é ilustrado considerando os vetores nome e nota ilustrados acima:
Index=[1, 2, 5, 7]
Observações:
- Considere a possibilidade do vetor Index não conter elementos, ou seja, não haver aprovados.
Neste caso, imprima uma mensagem relatando a situação e finalize o programa.
- No exemplo acima, os vetores tem tamanho 8, mas seu programa deve considerar que os
vetores nome e nota podem ter um tamanho qualquer, diferente de zero.
(Conceito utilizado: lista para armazenar índices de outra lista)'''

nome = ['Skywalker', "Kenobi", 'Solo', 'Vader', 'Organa', 'Amidala', 'Finn', 'Rey', 'Felipe']
nota = [5.8, 10.0, 8.5, 4.5, 3.2, 6.5, 3.5, 6.4, 8.0]

Index = []

for i in range(len(nota)):
    if nota[i] >= 6:
        Index.append(i)

if len(Index) == 0:
    print('\nNenhum aluno foi aprovado!\n')
else:
    print('\nAlunos Aprovados:\n')
    for i in range(len(Index)):
        print(f'{nome[Index[i]]}: {nota[Index[i]]}')

print()

'''
CHAT GPT

nome = ['Skywalker', "Kenobi", 'Solo', 'Vader', 'Organa', 'Amidala', 'Finn', 'Rey', 'Felipe']
nota = [5.8, 10.0, 8.5, 4.5, 3.2, 6.5, 3.5, 6.4, 8.0]

alunos_aprovados = [(n, nota[i]) for i, n in enumerate(nome) if nota[i] >= 6]

if len(alunos_aprovados) == 0:
    print('\nNenhum aluno foi aprovado!\n')
else:
    print('\nAlunos Aprovados:\n')
    for aluno, nota in alunos_aprovados:
        print(f'{aluno}: {nota}')

print()
'''
