# Escreva um programa em Python que solicite ao usuário o nome de um dia da semana e verifique
# se o dia é um dia útil (segunda a sexta-feira) ou um final de semana (sábado ou domingo).
# Funcionalidade Optativa: Considere que o usuário pode digitar o nome do dia com letras maiúsculas
# ou minúsculas.

print('\n*****DESCUBRA SE É UM DIA DA SEMANHA ÚTIL OU FINAL DE SEMANA*****\n')
dia = input('\nEntre com o dia da semana por extenso e sem hífen: \n').upper()

if dia == 'SEGUNDA' or dia == 'TERÇA' or dia == 'TERCA' or dia == 'QUARTA' or dia == 'QUINTA' or dia == 'SEXTA':
    print(f'\nO dia da semana digitado {dia} é um dia ÚTIL!\n')
elif dia == 'SÁBADO' or dia == 'SABADO' or dia == 'DOMINGO':
    print(f'\nO dia da semana digitado {dia} é no final de semana!\n')
else:
    print('\nNÃO É UM DIA DA SEMANA!\n')
