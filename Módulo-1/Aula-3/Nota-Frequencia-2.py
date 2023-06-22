# Faça um programa que solicita a nota (valor de 0 a 100) e a frequência de um aluno (um valor
# que representa o percentual) e verifica se ele foi aprovado ou reporvado. Para ser aprovado,
# precisa ter pelo menos 75 % de presença e ao menos 60 pontos. Verificar se os dados de entrada
# são válidos e finalizado caso não sejam válidos.

from time import sleep
nota = float(input('Digite a nota: '))
frequencia = float(input('Digite a frequência: '))

if (nota < 0 or nota > 100) or (frequencia < 0 or frequencia > 100):
    print('OS DADOS DIGITAS NÃO SÃO VÁLIDOS.Favor digitar novamente.')
    print('Encerrando o programa...')
    sleep(5)
else:
    if nota >= 60 and frequencia >= 75:
        print(f'Aluno(a) foi aprovado(a) com nota {nota:.2f} e frequência {frequencia:.0f}.')
    else:
        print(f'Aluno(a) Reprovado(a) com nota {nota:.2f} e frequência {frequencia:.0f}.')
