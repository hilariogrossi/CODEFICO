'''Na última aula de matemática Rafael, Beto e Carlos aprenderam algumas novas expressões matemáticas.
Cada um deles se identificou com uma expressão em especial e resolveram competir para ver quem tinha
a expressão de maior resultado.
* A expressão que Rafael escolheu é r = (3x)².
* Já Beto escolheu a expressão b = 2(x²) + (5y)².
* Carlos por sua vez escolheu a expressão c = -100x + y ** 3
Implemente uma função que receba os valores de x e y que calcule o valor de cada expressão e retorne
qual das expressões resultou no maior resultado. Para testar sua função implemente um programa
principal que leia N valores de x e y e para cada um deles imprima o vencedor.'''


def maior_resultado(x, y):
    r = (3 * x) ** 2
    b = 2 * (x ** 2) + (5 * y) ** 2
    c = -100 * x + y ** 3

    if r > b > c:
        return 'Rafael'
    elif b > r > c:
        return 'Beto'
    else:
        return 'Carlos'


N = int(input('\nEntre com o valor de N: '))

for i in range(N):
    X = int(input('\nForneça o valor de X: '))
    Y = int(input('\nForneça o valor de Y: '))

    nome = maior_resultado(X, Y)

    print(f'\nO vencedor foi o {nome}.\n')
