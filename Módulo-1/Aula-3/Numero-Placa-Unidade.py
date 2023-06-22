# Considere que o número de uma placa de veículo é composto por quatro algarismos. Por exemplo: 2018.
# Codifique um programa que leia esse número e exiba na tela o algarismo correspontente à casa das
# unidades.

placa = int(input('Digite o número da placa: '))

unidade = placa / 10
unidade_1 = unidade - int(unidade)
unidade_2 = round(unidade_1 * 10)
print(f'A unidade da placa digitada {placa} é {unidade_2}.')
