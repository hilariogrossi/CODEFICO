# Escreva um programa que leia o peso e a altura de uma pessoa e calcule seu IMC. Em seguida,
# exiba a classificação do IMC de acordo com a tabela a seguir:
# IMC abaixo de 18.5: Abaixo do peso
# IMC entre 18.5 e 24.9: Peso normal
# IMC entre 25.0 e 29.9: Sobrepeso
# IMC entre 30.0 e 34.9: Obesidade grau 1
# IMC entre 35.0 e 39.9: Obesidade grau 2
# IMC acima de 40.0: Obesidade grau 3 (mórbida)
# Cálculo IMC: O índice é calculado da seguinte maneira: divide-se o peso do paciente pela
# sua altura elevada ao quadrado.

peso = float(input('Entre com o peso em Kg: '))
altura = float(input('Entre com a altura em metros: '))

imc = peso / altura ** 2

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}, o que indica abaixo do peso.')
elif 18.5 <= imc <= 24.9:
    print(f'Seu IMC é {imc:.2f}, o que indica peso normal.')
elif 25.0 <= imc <= 29.9:
    print(f'Seu IMC é {imc:.2f}, o que indica sobrepeso.')
elif 30 <= imc <= 34.9:
    print(f'Seu IMC é {imc:.2f}, o que indica obesidade grau 1.')
elif 35 <= imc <= 39.9:
    print(f'Seu IMC é {imc:.2f}, o que indica obesidade grau 2.')
else:
    print(f'Seu IMC é {imc:.2f}, o que indica obesidade grau 3 (mórbida).')
