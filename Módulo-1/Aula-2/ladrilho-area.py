# Um pedreiro precisa calcular quantos ladrilhos devem ser comprados para
# cobrir a área de uma sala dada em cm². Implemente um programa que leia do
# teclado o tipo do ladrilho e a área da sala. O programa calcula e imprime o
# número de ladrilhos necessários. Imprima as saídas de dados de acordo com
# os exemplos de execução. As áreas de cada um dos tipos de ladrilhos
# disponíveis são dadas na tabela abaixo: Tipo 1 = 80 cm2 (um ladrilho)
# Tipo 2 = 60 cm2 (um ladrilho)

# Dica: Relembre as funções math.trunc(x), math.ceil(x) e math.floor(x) e
# escolha uma delas para obter a quantidade correta de ladrilhos após o
# cálculo (isso porque a divisão pode resultar em um valor real, mas a
# quantidade de ladrilhos é inteira, por exemplo, se o resultado for
# 4.1, 4.5, ou 4.9, a quantidade de ladrilhos necessária para todos os
# casos é 5).

import math

ladrilho = int(input('Forneça o tipo de ladrilho: [1] 80 cm2 ou [2] 60 cm2: '))
area = float(input('Digite a área da sala: '))

if ladrilho == 1:
    quantidade = math.ceil(area / 80)
elif ladrilho == 2:
    quantidade = math.ceil(area / 60)

print(f'A quantidade de ladrilhos é : {quantidade}.')
