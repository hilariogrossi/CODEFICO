'''O Índice de Massa Corporal, ou apenas IMC, é uma medida internacional que serve para
definir se uma pessoa está em seu peso ideal, abaixo ou acima dele. Uma classificação
simplificada do IMC é dada na tabela abaixo:
IMC:              Classificação:
IMC < 16          Magreza grave
16 <= IMC < 18,5  Abaixo do peso
18,5 <= IMC < 25  Saudável
25 <= IMC < 30    Sobrepeso
30 <= IMC < 40    Obesidade
IMC >= 40         Obesidade extrema
Sabendo que o cálculo do IMC é dado pela fórmula IMC = peso/(altura x altura), fazer um
programa para classificar a condição de um dado número de pacientes. O programa deve
inicialmente ler o total de pacientes (inteiro) e depois, para cada paciente, ler o
peso e altura (reais), calcular o seu respectivo IMC e imprimir na tela a sua classificação,
de acordo com a tabela anterior. Ao final o programa deve informar o percentual de pacientes
contidos em duas classes: “Magreza grave” e “Obesidade extrema”. Todos os valores calculados
devem ser exibidos com formatação de 2 casas decimais. '''

total_paciente = int(input('\nInforme a quantidade de paciênte(s): '))
magreza_grave = obsesidade_extrema = 0

for i in range(1, total_paciente + 1):
    peso = float(input(f'\nInforme o peso do {i}° paciente: '))
    altura = float(input(f'\nInforme a altura do {i}° paciente: '))

    IMC = peso / altura ** 2

    if IMC < 16:
        condicao = 'Magreza Grave'
        magreza_grave += 1
    elif 16 <= IMC < 18.5:
        condicao = 'Abaixo do peso'
    elif 18.5 <= IMC < 25:
        condicao = 'Saudável'
    elif 25 <= IMC < 30:
        condicao = 'Sobrepeso'
    elif 30 <= IMC < 40:
        condicao = 'Obesidade'
    else:
        condicao = 'Obesidade extrema'
        obsesidade_extrema += 1

    print(f'\nIMC = {IMC:.3f}  e sua condição é: {condicao}.')

percentual_magreza_grave = magreza_grave / total_paciente * 100
percentual_obesidade_extrema = obsesidade_extrema / total_paciente * 100

print(f'\nO percentual de Magreza Grave é: {percentual_magreza_grave} %.')
print(f'\nO percentual de Obesidade Extrema é: {percentual_obesidade_extrema} %.\n')
