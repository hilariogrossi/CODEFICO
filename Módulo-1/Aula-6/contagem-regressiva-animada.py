# Contagem regressiva animada. Escreva um programa em Python que utilize o comando while para
# exibir uma contagem regressiva animada. O programa deve solicitar ao usuário quantos segundos
# deseja na contagem regressiva e, em seguida, iniciar a contagem regressiva a partir desse valor,
# exibindo cada número na tela e aguardando um segundo entre cada número.

from time import sleep

segundos = int(input('\nQuantos segundos deseja na contagem regressiva? '))

print('\nIniciando contagem regresiva...\n')

sleep(1)

cont = segundos

while cont > 0:
    print(f'{cont}')
    sleep(1)
    cont -= 1

print('\nBoom! FELIZ ANO NOVO!\n')
