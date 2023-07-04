'''Em uma eleição presidencial existem quatro candidatos, sendo eles João(1), Maria(2), Lucas(3),
Luísa(4). Os votos são informados por meio de código para seus devidos candidatos. E teremos também
o voto nulo(5), voto em branco(6) e encerrar votação(0). Faça um menu exibindo os códigos e seus
valores e exiba no final os seguintes dados:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos.
Total de votos
Para finalizar o conjunto de votos tem-se o valor zero.'''


def calcular_percentagem(total, votos):
    if total == 0:
        return 0
    return (votos/total) * 100

# Iniciar Variaveis
votos_joao = 0
votos_maria = 0
votos_lucas = 0
votos_luisa = 0
votos_nulos = 0
votos_brancos = 0
total_votos = 0

print('\nMenu de Votação:')
print('1 - João')
print('2 - Maria')
print('3 - Lucas')
print('4 - Luísa')
print('5 - Voto Nulo')
print('6 - Voto em Branco')
print('0 - Encerrar Votação')

while True:
    voto = int(input('\nDigite o código do candidato: '))

    if voto == 0:
        break

    total_votos += 1

    if voto == 1:
        votos_joao += 1
    elif voto == 2:
        votos_maria += 1
    elif voto == 3:
        votos_lucas += 1
    elif voto == 4:
        votos_luisa += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_brancos += 1

print('\nResultado da Eleição:')
print(f'\nJoão: {votos_joao} voto(s)')
print(f'\nMaria: {votos_maria} voto(s)')
print(f'\nLucas: {votos_lucas} voto(s)')
print(f'\nLuísa: {votos_luisa} voto(s)')

percentagem_nulos = calcular_percentagem(total_votos, votos_nulos)
percentagem_brancos = calcular_percentagem(total_votos, votos_brancos)

print(f'\nVoto(s) Nulo(s): {percentagem_nulos:.2f}%')
print(f'\nVoto(s) em Branco(s): {percentagem_brancos:.2f}%')

print(f'\nTotal de voto(s): {total_votos}\n')
