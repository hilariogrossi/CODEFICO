'''O Campus Aberto da UFOP realizará uma gincana e precisa de um programa para computar a
pontuação das duas equipes participantes e determinar a equipe vencedora, da seguinte forma:
1.  Serão realizadas N provas, definidas por entrada do usuário;
2.  Cada equipe receberá uma nota entre 0 e 10 para cada prova (não é necessário validar);
3.  A equipe com maior pontuação será a vencedora da prova, podendo haver empate;
4.  Para cada prova, deverá ser lida a nota de cada equipe e computada a equipe vencedora;
5.  Ao final informar qual foi a equipe que venceu o maior número de provas, ou se houve empate;
6.  O programa imprime a pontuação de cada equipe e a equipe vencedora na tela.
Obs.: quanto ao ponto 6, não computar notas totais. Não é para imprimir as notas parciais.'''

N = int(input('\nQuantas provas serão realizadas? '))
ponto_total_equipe_1 = ponto_total_equipe_2 = empate = 0

for i in range(1, N + 1):
    print(f'\n*****{i}° PROVA****')
    nota_equipe_1 = float(input('\nEntre com a nota da equipe 1: '))
    nota_equipe_2 = float(input('\nEntre com a nota da equipe 2: '))

    if nota_equipe_1 > nota_equipe_2:
        ponto_total_equipe_1 += 1
    elif nota_equipe_2 > nota_equipe_1:
        ponto_total_equipe_2 += 1
    else:
        empate += 1

print(f'\nA equipe 1 venceu {ponto_total_equipe_1} prova(s).')
print(f'\nA equipe 2 venceu {ponto_total_equipe_2} prova(s).')
print(f'\nHouve {empate} empate(s).')

if ponto_total_equipe_1 > ponto_total_equipe_2:
    print('\nA equipe 1 é a vencedora.\n')
elif ponto_total_equipe_2 > ponto_total_equipe_1:
    print('\nA equipe 2 é a vencedora.\n')
elif ponto_total_equipe_1 == ponto_total_equipe_2:
    print('HOUVE EMPATE ENTRE AS DUAS EQUIPES!')
