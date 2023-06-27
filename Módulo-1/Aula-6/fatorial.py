# Você foi contratado por uma empresa química que precisa resolver algumas fórmulas matemáticas para desenvolver produtos químicos.
# Você foi o escolhido para encontrar o fatorial de um número. Calcular o fatorial de um número só faz sentido quando estamos trabalhando com números naturais.
# Essa operação é bastante comum na análise combinatória, facilitando o cálculo de arranjos, permutações, combinações e demais problemas envolvendo contagem.
# O fatorial é representado pelo símbolo "!". Definimos como n! (n fatorial) a multiplicação sucessiva de n por todos os seus antecessores até chegar em 1.
# A equação do fatorial pode ser definida como: n! = n × (n − 1) × (n − 2) × ... × 3 × 2 × 1. Observe que o número definido é sempre inteiro, mas o programa
# "força" a entrada de um número maior do que 0 (zero).

num = int(input('Entre com o número para calcular o fatorial: '))

cont = num
fatorial = 1

print(f'{num}! = ', end='')

while cont > 0:
    fatorial *= cont
    print(f'{cont} ', end='')
    print('X ' if cont > 1 else '= ', end='')
    cont -= 1

print(f'{fatorial}')

#print(f'O {num}! = {fatorial}')
