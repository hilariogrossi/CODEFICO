'''Problema do Decifrador de Senhas. Um determinado banco fornece aos seus clientes, além da senha 
numérica, uma senha de 3 letras que deve ser utilizada no caixa eletrônico na realização de operações.
O software do caixa eletrônico, para dificultar a ação de ladrões, solicita a entrada da senha de 3
letras em um "teclado" gráfico especial gerado aleatoriamente todas as vezes e exibido na tela do 
monitor. Neste teclado, cada uma das teclas contém uma quantidade de 4 letras distintas. Para 
digitar a senha, o usuário deve escolher em ordem as teclas que contenham as letras da sua senha. 
Por exemplo, sendo a senha ABC e existindo as teclas MNAU, ILKC, JIYB e OKLM o usuário deve 
pressionar as teclas MNAU, JIYB e ILKC nesta ordem. Um contraventor observou determinados usuários 
do banco durante várias operações no caixa eletrônico e anotou as teclas pressionadas durante a 
operação. O banco, que grava a cada operação as teclas pressionadas pelo usuário, foi informado da 
atuação de tal criminoso e deseja fazer um programa para saber de quais clientes é necessário 
bloquear a senha. As senhas bloqueadas serão aquelas que, a partir das teclas pressionadas, o 
contraventor é capaz de saber, sem sombra de dúvida, qual é a senha de 3 letras do cliente.
Faça um programa que receberá 9 cadeias de caracteres do mesmo tamanho de um arquivo chamado: 
entrada.txt. Cada bloco de 3 cadeias conterá as letras das "teclas" gráficas pressionadas pelo 
usuário com relaçao a uma letra da senha. O primeiro bloco de 3 cadeias irá conter as teclas 
pressionadas com relação à primeira letra da senha, o segundo bloco as teclas pressionadas com 
relação à segunda e o terceiro bloco as teclas pressionadas com relação à terceira letra da senha. 
O programa deverá retornar 1 caso seja possível identificar (sem sombra de dúvidas) quais as letras 
da senha e 0 caso contrário.

EXEMPLO 1
Arquivo: entrada.txt
MNAU
LACN
AKIM
IKJH
ILKC
JKBM
MUDH
ADIK
HUDM

Saída:
1

A senha do exemplo 1 seria AKD, percebam que nas três primeiras entradas a letra que mais se repete 
é A. Da 4 a 6 entrada temos o K e da 7 a 9 entrada temos a letra D. Não é necessário retornar a 
senha. A saída somente é 0 ou 1.'''

with open('entrada.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

for i, elemento in enumerate(linhas):
    elemento = elemento.replace('\n', '')

bloco_1 = linhas[0:3]
bloco_2 = linhas[3:6]
bloco_3 = linhas[6:9]


def ocorrencia_letra(string_1, string_2, string_3, letra):
    posicao_1 = string_1.find(letra)
    posicao_2 = string_2.find(letra)
    posicao_3 = string_3.find(letra)

    if posicao_1 >= 0 and posicao_2 >= 0 and posicao_3 >= 0:
        return 1
    else:
        return 0


def ocorrencia(B):
    #B = bloco_1, bloco_2 bloco_3
    for e in B[0]:
        boolB = ocorrencia_letra(B[0], B[1], B[2], e)

        if (boolB == 1):
            return e

    return ''


def ocorrencia_senha(B1, B2, B3):
    variavel_B1 = ocorrencia(B1)
    variavel_B2 = ocorrencia(B2)
    variavel_B3 = ocorrencia(B3)

    if (variavel_B1 and variavel_B2 and variavel_B3) != '':
        return 1
    else:
        return 0

print(ocorrencia_senha(bloco_1, bloco_2, bloco_3))
