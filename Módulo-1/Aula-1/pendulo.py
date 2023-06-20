'''Você participará de um processo seletivo para estagiário do Dr.Spock na USS Enterprise, e precisa cumprir um desafio proposto por ele a fim de mostrar
suas habilidades como programador. Ele quer que você implemente um programa que vai calcular o período de um pêndulo simples. Para isso, ele te passou a seguinte
equação matemática: T = 2 * π * (L/g) ** 0.5 onde: π é a constante de valor 3, 14; L é o comprimento do fio; e g é a aceleração da gravidade no planeta.
Você não conhece a aceleração de gravidade do planeta onde está, mas consegue calculá-la pela equação: g = P / m
onde: P é a força peso e m é a massa.

O seu programa receberá, como entradas do usuário, os seguintes valores reais: L, P e m. Em seguida, ele calculará a aceleração de gravidade do planeta (g)
e o período do pêndulo simples (T). Imprimindo os resultados, conforme os exemplos a seguir, com uma precisão matemática de 3 casas decimais na saída.

Dica: para calcular a raiz quadrada de um número você pode eleva-lo à potência 0,5,
ou seja, √ x = x 0,5'''

from math import pi, sqrt

L = float(input('Forneça o comprimento do fio: '))
P = float(input('Forneça a força peso: '))
m = float(input('Forneça a massa: '))

g = P / m

T = 2 * pi * sqrt(L/g)

print(f'A aceleração da gravidade é: {g:.3f}')
print(f'O período do pêndulo é: {T:.3f}')
