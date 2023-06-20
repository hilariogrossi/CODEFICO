''' Progressão geométrica é uma sequência numérica que possui uma razão fixa denominada (q) onde, a partir da definição do primeiro termo (a1) os termos
 subsequentes são calculados individualmente pela razão (q) multiplicada pelo seu antecessor. Para determinar um termo qualquer desta sequência, não é
 necessário calcular todos os seus antecessores a partir do primeiro termo, você pode obter o termo (an) conhecendo apenas o termo inicial (a1)
 e a razão (q) aplicando a equação:an = a1 * q ** (n-1). Implemente um programa que leia, como entradas dos usuários, os valores reais representando
 o primeiro termo (a1) e a razão (q), o valor inteiro representando o número (n). O programa calcula o valor do termo (an) e imprime o resultado
 no terminal com uma precisão de 2 casas decimais.'''

a1 = float(input('Informe o primeiro termo: '))
q = float(input('Informe a razão: '))
n = int(input('Informe o número do termo: '))

an = a1 * q ** (n-1)

print(f'O termo a({n}) é: {an:.2f}')
