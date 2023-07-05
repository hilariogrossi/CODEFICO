'''Implemente um programa que faça o calculo da soma de dois digitos de um número. Por exemplo,
a soma dos dígitos do número 23: 2 + 3 = 5. Faça esse programa criando uma função chamada
soma_digitos(numero) que recebe a variável numero como parâmetro. Dica: Caso necessário utilize
o operador (//). Ele é um operador que pega a divisão inteira entre dois números. Utilizamos
ele da seguinte forma: numero1//numero2 = resultado'''


def soma_digitos(numero):
    unidade = numero % 10
    resto = numero // 10

    soma = unidade + resto

    return soma


num = int(input('\nEntre com o número: '))

soma_total = soma_digitos(num)

print(f'A soma dos dígitos é: {soma_total}\n')
