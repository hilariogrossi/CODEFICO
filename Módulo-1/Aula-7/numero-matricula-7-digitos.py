''' Um número de matrícula da universidade é composto por 7 dígitos, como: 21.1.5423
Os primeiros dois dígitos representam o ano de entrada na universidade (Exemplo: 21)
O terceiro dígito representa o semestre. Os dígitos restantes representam a a identificação do
estudante em relação às matrículas do semestre. Faça um programa que solicite ao usuário a entrada
de um número de matrícula em formato de um número inteiro. Seu programa deve validar o ano
e também o terceiro algarismo. Qualquer valor de ano que seja maior ou igual a 75 (representa o
ano 1975) e menor ou igual a 21 (representa o ano 2021) será um valor de ano válido. Para o
dígito que representa o semestre apenas os valores 1 e 2 serão válidos. Ao final o programa
deve imprimir se o número de matrícula é válido ou não.''' 

matricula = input('Entre com seu número de matrícula com 7 digitos (sem traços): ')

ano = int(matricula[0:2])
semestre = int(matricula[3])
numero_restante = int(matricula[3:7])

if (semestre == 1 or semestre == 2) and (0 <= ano <= 21) or (75 <= ano <= 99):
    print(f'\nO número de matrícula {matricula} está VALIDADO!\n')
else:
    print(f'\nO número de matrícula {matricula} NÃO ESTÁ validado!\n')
