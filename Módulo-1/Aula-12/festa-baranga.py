'''No próximo final de semana ocorrerá a badalada Festa Baranga da UFOP. O ingresso masculino será
de R$ 12,50 e o feminino será de R$ 7,40. Um calouro ficou encarregado de operar um programa na
portaria do ginásio para controlar o acesso das pessoas à festa. O programa é executado da seguinte
forma: * quando chega um homem na festa ele digita 'h' * quando chega uma mulher na festa ele digita
'm' * quando o calouro quiser encerrar a entreda de dados ele digita 'q' * o calouro não tem noção
de quantas pessoas irão à festa. No momento que a entrada de dados for encerrada o programa calcula
quanto foi arrecadado. Seu programa deve seguir o seguinte modelo de execução observando os formatos
de impressão:
Festa Baranga, Again!
----------------------
Quem chegou? (h/H/m/M/q?q) ----> h'''

print('\nFesta Baranga, Again!')
print('------------------------')

pergunta = input('\nQuem chegou? (h/H/m/M/Q/q) ----> ')

contaH = contaM = 0

while pergunta == 'H' or pergunta == 'h' or pergunta == 'M' or pergunta == 'm':
    if pergunta == 'H' or pergunta == 'h':
        contaH += 1
    else:
        contaM += 1
    
    pergunta = input('\nQuem chegou? (h/H/m/M/Q/q) ----> ')

totalH = 12.50 * contaH
totalM = 7.40 * contaM

print(f'''
A quantidade de homem foi {contaH}.
A quantidade de mulher foi {contaM}
O total arrecadado com homem foi R$ {totalH:8.2f}.
O total arrecadado com mulher foi R$ {totalM:8.2f}
O total geral arrecadado foi R$ {totalH + totalM:8.2f}\n''')
