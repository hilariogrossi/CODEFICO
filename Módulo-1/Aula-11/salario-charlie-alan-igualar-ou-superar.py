'''Escreva um rograma que receba o salário de um funcionário Charlie. Sabe-se que outro
funcionário, Alan, tem salário igual a um terno do salário de Charlie. Charlie aplicará seu salário
integralmente na cardeneta de poupança que está rendendo 0.5 % ao mês e Alan aplicará seu salário
integralmente no fundo de renda fixa cujo percentual de rendimento deve ser solicitado na entrada
do programa. O programa deverá calcular e mostrar a quantidade de meses necessários para que o
valor pertencente a Alan iguale ou ultrapasse o valor pertencente a Charlie. Caso o valor seja
menor que 0,5 %, ou igual, o programa deve mostrar um mensagem dizendo que a aplicação de Alan
nunca alcançará o valor da aplicação do Charlie e finalizar.'''

salario_charlie = float(input('\nInforme o salário do Charlie: R$ '))
salario_alan = salario_charlie / 3
rendimento = float(input('\nInforme o percentual de rendimento ao mês: '))

if rendimento <= 0.5:
    print('A aplicação de Alan nunca alcançará o valor da aplicação do Charlie')
else:
    meses = 0

    while salario_alan <= salario_charlie:
        meses += 1
        salario_charlie += salario_charlie * 0.5 / 100
        salario_alan += salario_alan * rendimento / 100

    print(f'\nInvestimento Charlie: R$ {salario_charlie:.2f}\nInvestimento Alan: R$ {salario_alan:.2f}')
    print(f'\nA quantidade de meses: {meses}\n')
