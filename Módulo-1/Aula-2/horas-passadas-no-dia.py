# Crie um programa que leia um valor de hora (hora:minutos) e informe (calcule) o total de minutos que se passaram desde o início do dia (0:00h)

hora = int(input('Entre com a hora: '))
minuto = int(input('Entre com os minutos: '))

total = hora * 60 + minuto

print(f'O tempo total passado foi de {total} minutos.')
