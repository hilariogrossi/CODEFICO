'''Faça um programa que ache o número menor e o maior de uma série de 10 elementos digitados pelo
usuário usando for. Use números inteiros e positivos'''

numero_menor = numero_maior = 0

for i in range(10):
    numeros_usuario = int(input(f'\nEntre com o {i + 1}° número: '))

    if (i + 1) == 1:
        numero_menor = numero_maior = numeros_usuario
    else:
        if numeros_usuario > numero_maior:
            numero_maior = numeros_usuario
        elif numeros_usuario < numero_menor:
            numero_menor = numeros_usuario

print(f'\nO menor número digitado é: {numero_menor} e o maior é: {numero_maior}.\n')
