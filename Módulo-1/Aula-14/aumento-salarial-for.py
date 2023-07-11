'''Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00; Em 1996 recebeu aumento
de 1,5% sobre seu salário inicial; A partir dos proximos anos, os aumentos salariais sempre
correspondem ao percentual do ano anterior + 0.0025 . Faça um programa que determine o salário
atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite
o salário inicial do funcionário. Obs.: considere que todos os funcionários sao contratados no
início do ano e o percentual de aumento só aumenta ao final do ano.'''

salario = float(input('\nDigite o salário inicial: R$ '))
ano_contratacao = int(input('\nEntre com o ano de contratação: '))
ano_atual = int(input('\nEntre com o ano atual com 4 dígitos: '))
aumento = 1.5 / 100

for ano in range(ano_contratacao + 1, ano_atual):
    salario += salario * aumento
    aumento += 0.0025

print(f'\nO salário atual do funcionário é R$ {salario:.2f} em {ano_atual}\n')
