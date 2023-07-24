'''Você é um programador experiente que trabalha em uma empresa de desenvolvimento de software. 
Seu gerente de projeto atribuiu a você a tarefa de criar uma função em Python que receba duas tuplas
como argumentos e retorne uma nova tupla contendo a concatenação das duas tuplas. Essa função será 
utilizada em um projeto maior, que envolve manipulação de dados em tuplas.
Passo 1: Crie duas tuplas manualmente.
Passo 2: Crie uma função que receba as tuplas e retorne uma tupla que represente a concatenação das duas.
Passo 3: A concatenação das tuplas dentro da função pode ser feita pelo operador "+" ou por um laço de repetição, adicionando item por item.
Passo 4: Imprima a tupla retornada.
Exemplo: Entrada: A entrada será as duas tuplas criadas no código. Exemplo: (1, 3, 6) e (7, 5, 2)
Saída: (1, 3, 6, 7, 5, 2)'''

def projeto_tuplas(tupla_1, tupla_2):
    return tupla_1 + tupla_2


tupla_1_1 = 1, 3, 6
tupla_2_1 = 7, 5, 2

resultado = projeto_tuplas(tupla_1_1, tupla_2_1)

print(f'\nA concatenação tem como resultado: {resultado}\n')
