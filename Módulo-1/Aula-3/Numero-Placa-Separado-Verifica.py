# Considere que o número de uma placa de veículo é composto por quatro algarismos; por exemplo 2018.
# Codifique um programa que leia este número e exiba na tela todos os 4 algarismos da placa,
# separadamente. Faça a validação da entrada para garantir que o número informado pode representar
# um número de placa no formato indicado.

placa = int(input('Digite o número da placa: '))

if placa < 0 or placa > 9999:
    print(f'O número de placa informado "{placa}" está no formato errado. por favor digite novamente!')

algarismo_1 = int(placa / 1000)
temporario_1 = placa % 1000
algarismo_2 = int(temporario_1 / 100)
temporario_2 = placa % 100
algarismo_3 = int(temporario_2 / 10)
algarismo_4 = int(temporario_2 % 10)
print(f'Os algarismos da placa {placa} são {algarismo_1}, {algarismo_2}, {algarismo_3} e {algarismo_4}.')
