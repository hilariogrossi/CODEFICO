'''
Codifique um programa que realize as seguintes tarefas:
1) leia 4 números reais pelo teclado,  com 1 ≤ i ≤ 4; Ou seja, n = 4
2) calcule a média aritmética M, dos números lidos:
3) calcule o desvio padrão D, dos números lidos. O cálculo do desvio padrão é
realizado através dos seguintes passos, com 1 ≤ i ≤ 4:
a)	calcule o somatório das parcelas ( - M)2;
b)	multiplique o resultado do item a) por 1 / (n - 1);
c)	extraia a raiz quadrada do resultado do passo b), obtendo-se o desvio padrão.
A fórmula que resume os passos 1, 2 e 3 é:
4) imprima o valor da média aritmética e do desvio padrão conforme o exemplo de execução
exibido abaixo.
5) a média aritmética e o desvio padrão devem ser implementadas por Funções Definidas
Pelo Usuário, por exemplo, MediaAritmetica e DesvioPadrao, respectivamente.
OBS.: não é necessária a validação dos dados de entrada, considere que as coordenadas
serão sempre números reais.
(Conceito utilizado: um programa cheio de detalhes)
'''
import math


def mediaAritmetica(X1, X2, X3, X4):
    M = ((X1 + X2 + X3 + X4)) / 4

    return M


def desvioPadrao(X1, X2, X3, X4, ma):
    soma = ((X1 - ma) ** 2 + (X2 - ma) ** 2 + (X3 - ma) ** 2 + (X4 - ma) ** 2)
    multiplicacao = soma * 1 / (4 - 1)

    D = math.sqrt(multiplicacao)

    return D


x1 = float(input('\nEntre com o valor de X1: '))
x2 = float(input('\nEntre com o valor de X2: '))
x3 = float(input('\nEntre com o valor de X3: '))
x4 = float(input('\nEntre com o valor de X4: '))

media = mediaAritmetica(x1, x2, x3, x4)
desvio = desvioPadrao(x1, x2, x3, x4, media)

print('\nIMPRESSÃO DE RESULTADOS:')
print(f'\nMédia Aritmética é: {media:.2f}\n\nDevio Padrão é: {desvio:.5f}\n')
