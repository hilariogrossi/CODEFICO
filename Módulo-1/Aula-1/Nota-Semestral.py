'''A nota semestral dos alunos é obtida de acordo com o cálculo descrito a seguir: NS = AV1 + AV2, onde:

AV1 = 0, 3 × P T1 + 0, 15 × EP1;
AV2 = 0, 4 × P T2 + 0, 15 × EP2;
PT1 e PT2 são provas teóricas unificadas, com nota entre 0 e 10;
EP1 e EP2 são atividades distribuídas pelos professores, com nota entre 0 e 10.

Implemente um programa que leia, como entradas dos usuários, os valores reais das notas P T1, P T2, EP1 e EP2. O programa calcula o valor das avaliações parciais
AV1 e AV2, e da nota do semestre NS. Em seguida, ele imprime os resultados no terminal com uma precisão de 2 casas decimais.'''

pt1 = float(input('Informe a nota PT1: '))
ep1 = float(input('Informe a nota EP1: '))
pt2 = float(input('Informe a nota PT2: '))
ep2 = float(input('Informe a nota EP2: '))

av1 = 0.3 * pt1 + 0.15 * ep1
av2 = 0.4 * pt2 + 0.15 * ep2

ns = av1 + av2

print(f'A nota na AV é: {av1:.2f}!')
print(f'A nota na AV2 é: {av2:.2f}!')
print(f'A nota no semestre é: {ns:.2f}!')
