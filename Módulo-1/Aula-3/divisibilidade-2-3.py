# Questão: Divisibilidade por 2 e 3
# Escreva um programa que leia um número inteiro e verifique se ele é divisível por 2 e por 3.
# Caso seja, exiba a mensagem "O número é divisível por 2 e por 3".
# Caso contrário, se for divisível apenas por 2, exiba a mensagem "O número é divisível por 2,
# mas não por 3".
# Caso não seja divisível por 2, exiba a mensagem "O número não é divisível por 2".

num = int(input('Entre com o número a ser analisado: '))

if num % 2 == 0 and num % 3 == 0:
    print('\nO número é divisível por 2 e por 3.\n')
elif num % 2 == 0:
    print("\nO número é divisível por 2, mas não por 3.\n")
else:
    print("\nO número não é divisível por 2.\n")
