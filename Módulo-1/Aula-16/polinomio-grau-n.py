'''Seja o polinômio de grau n, assim definido:
P(x) = a1 + a2*x**1 + a3*x**2 + a4*x**3 + ... + an*x**(n-1) + an+1*x**n
Escreva um programa que solicite ao usuário o vetor de coeficientes A, que pode ter
qualquer tamanho. Exemplo: A = [2.3 -4.5 0 3.8]
Em seguida, o programa deverá ler um valor para x, calcular e imprimir o valor de P(x).
Deverá imprimir, também, os componentes do polinômio, que devem estar em um vetor.
Observação: o vetor do exemplo acima contém dados de um polinômio de grau 3, mas seu
programa deve estar preparado para tratar um polinômio de qualquer grau.
(Conceito utilizado: séries envolvendo listas)'''

entrada = input('\nEntre com a lista dos coeficiêntes (somente números): ')
coeficiente = entrada.split()
x = float(input('\nEntre com  valor de x: '))
P = 0 # polinômio
V = [] # vetor

for i in range(len(coeficiente)):
    V.append(float(coeficiente[i]) * x ** i)
    P += float(coeficiente[i])

print(f'\nP(x) = {P:.5f}. Os componentes de P(x) foram: ', end=' ')
print(f'{V}\n')
