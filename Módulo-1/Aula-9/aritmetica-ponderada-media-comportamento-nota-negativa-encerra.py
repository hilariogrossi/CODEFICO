'''Em um novo arquivo faça um novo programa principal para usar a função do programa
aritmetica-ponderada-media-comportamento.py . O novo programa principal deve solicitar ao usuário
valores para um conjuto de estudantes. Para cada estudante deve haver a entrda dos dados e a 
chamada à função usando os parâmetros de cada aluno. O programa termina caso uma das notas
para um dado estudante seja menor que zero.'''


def CalculaNota(x1, x2, x3, l):
    aritmetica = (x1 + x2 + x3) / 3
    ponderada = x1 * 0.2 + x2 * 0.35 + x3 * 0.45

    if l == 'B' and ponderada > aritmetica:
        return ponderada, 'PONDERADA'
    else:
        return aritmetica, 'ARITMÉTICA'


print('\nNOVO ALUNO!')
n1 = float(input('\nDIGITE A NOTA 1: '))
n2 = float(input('\nDIGITE A NOTA 2: '))
n3 = float(input('\nDIGITE A NOTA 3: '))

letra = input('\nDIGITE A LETRA QUE INDICA PARTICIPAÇÃO (B/R): ').upper()

while letra != 'B' and letra != 'R':
    letra = input('\nERRO! Entre com [B] boa e [R] ruim: ').upper()

while n1 >= 0 and n2 >= 0 and n3 >= 0:
    nota, metodo = CalculaNota(n1, n2, n3, letra)

    print(f'\nNOTA FINAL DO ALUNO: {nota:.2f}')

    if nota >= 6:
        print('\nALUNO APROVADO')
    else:
        print('\nALUNO REPROVADO.')

    print(f'\nSUA NOTA FOI CALCULADA USANDO A MÉDIA {metodo}!')

    print('\nNOVO ALUNO!')

    n1 = float(input('\nDIGITE A NOTA 1: '))
    n2 = float(input('\nDIGITE A NOTA 2: '))
    n3 = float(input('\nDIGITE A NOTA 3: '))

    letra = input('\nDIGITE A LETRA QUE INDICA PARTICIPAÇÃO (B/R): ').upper()

print('\nO PROGRAMA FOI ENCERRADO!\n')
