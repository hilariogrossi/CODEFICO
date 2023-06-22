# Escreva um programa que leia um número inteiro e verifique se ele está no intervalo de 50 a 100,
# inclusive. Se o número estiver nesse intervalo, exiba a mensagem "O número está entre 50 e 100".
# Caso contrário, exiba a mensagem "O número não está entre 50 e 100".

num = int(input('Entre com um número para verificação: '))

if 50 <= num <= 100:
    print("O número está entre 50 e 100.")
else:
    print("O número não está entre 50 e 100.")
