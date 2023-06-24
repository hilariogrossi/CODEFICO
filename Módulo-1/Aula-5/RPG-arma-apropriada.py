# Um programa está sendo desenvolvido para ajudar um jogador de RPG a escolher a melhor arma com base em seu nível de experiência.
# As regras para determinar a arma recomendada são as seguintes:
# Se o nível de experiência do jogador for menor que 10, a arma recomendada é a "Espada Curta".
# Se o nível de experiência estiver entre 10 e 20 (inclusive), a arma recomendada é o "Machado de Batalha".
# Se o nível de experiência estiver entre 21 e 30 (inclusive), a arma recomendada é o "Martelo de Guerra".
# Se o nível de experiência for maior que 30, a arma recomendada é a "Espada Lendária".
# Escreva um programa que solicita ao jogador seu nível de experiência e, com base nas regras
# acima, exiba a arma recomendada. Dica: Utilize as estruturas if, elif e else para verificar as
# condições e os operadores >, <, >= para realizar as comparações necessárias.

print('\nEscolha sua adequada arma pelo seu nível de experiência de 0 - 100 %\n')
experiencia = int(input('\nQual o seu nível de experiência? '))

if 0 <= experiencia < 10:
    print('\nA arma recomentada é a "Espada Curta"!\n')
elif 10 <= experiencia <= 20:
    print('\nA arma recomendada é o "Machado de Batalha"!\n')
elif 21 <= experiencia <= 30:
    print('\nA arma recomendada é o "Martelo de Guerra"!\n')
elif 31 <= experiencia <= 100:
    print('\nA arma recomendada é o "Espada Lendária"!\n')
else:
    print('\nNÃO EXISTE ESSE NÍVEL DE EXPERIÊNCIA. Encerrando o programa...\n')
