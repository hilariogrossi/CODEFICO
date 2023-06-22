# Uma empresa de locação de veículos utiliza os seguintes valores para locação de um veículo:
# R$ 1,00 para os primeiros 100 km rodados;
# R$ 0,80 para os próximos 200 km rodados e
# R$ 0,70 para a quilometragem acima de 300 km.
# Escreva um rpograma que tenha como entrada a quilometragem percorrida por um veículo e que
# calcule o custo total da locação e o custo médio por quilômetro percorrido por esse veículo.

km = float(input('Entre com a quantidade de quilômetros rodados: '))

if km <= 0:
    print('Quilometragem errada! Informe novamente...')
else:
    if km <= 100:
        valor = km
    elif km <= 300:
        valor = km + (km - 100) * 0.8
    else:
        valor = 100 + 200 * 0.8 + (km - 300) * 0.7
    print(f'Custo de locação do veículo é R$ {valor:.2f} e Custo médio por quilômetro R$ {valor / km:.2f}.')
