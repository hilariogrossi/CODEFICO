def calculaNota(n1, n2, n3, participacao):
    aritmetica = (n1 + n2 + n3) / 3
    ponderada = n1 * 0.2 + n2 * 0.35 + n3 * 0.45

    if participacao == 'B' and ponderada > aritmetica:
        return ponderada, 'PONDERADA'
    else:
        return aritmetica, 'ARITMÉTICA'


nota_1 = float(input('\nEntre com a primeira nota do aluno: '))
nota_2 = float(input('\nEntre com a segunda nota do aluno: '))
nota_3 = float(input('\nEntre com a terceira nota do aluno: '))

participacao = input('\nEntre com [B] boa e [R] ruim para a participação do aluno: ').upper()

resposta, metodo = calculaNota(nota_1, nota_2, nota_3, participacao)

if resposta >= 6:
    print(f'\nO aluno foi aprovado com {resposta:.2f} e utilizando a média {metodo}!\n')
else:
    print(f'\nO aluno foi reprovado com {resposta:.2f} e utilizando a média {metodo}!\n')
