'''Escreva uma função chamada 'verificar_soma_par_impar' que recebe dois valores inteiros, 'valor1'
e 'valor2'. A função deve calcular a soma desses valores e determinar se a soma é par ou ímpar.
Em seguida, a função deve retornar 'P' se a soma for par, ou 'I' se a soma for ímpar. Na função
principal do seu programa solicite ao usuário dois números entre 0 e 10, inclusivamente.
Se o usuário fornecer um valor fora desse intervalo, o programa deve encerrar. Caso contrário,
a função 'verificar_soma_par_impar' deve ser chamada. A função 'verificar_soma_par_impar' determina
se a soma dos dois números é par ou ímpar. Se a soma for par, a função retorna 'P'; se for ímpar,
a função retorna 'I'. Com base no resultado retornado, a função principal deve exibir a seguinte
mensagem na tela: Se o resultado for 'P', imprima: 'A soma dos valores é par.' Se o resultado for
'I', imprima: 'A soma dos valores é ímpar.'''


def verificar_soma_par_impar(valor1, valor2):
    soma = valor1 + valor2

    if soma % 2 == 0:
        return 'P'
    else:
        return 'I'


v1 = int(input('\nEntre com um número entre [0 - 10]: '))
v2 = int(input('\nEntre com outro número entre [0 - 10]: '))

if 0 <= v1 <= 10 and 0 <= v2 <= 10:
    resultado = verificar_soma_par_impar(v1, v2)

    if resultado == 'P':
        print('\nA soma dos valores é par.\n')
    elif resultado == 'I':
        print('\nA soma dos valores é ímpar.\n')
else:
    print('\nNÚMEROS INVÁLIDOS. Encerrando programa...\n')
