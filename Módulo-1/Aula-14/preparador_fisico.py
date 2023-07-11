'''O preparador físico de um atleta de maratona deseja calcular o tempo estimado para completar
uma prova com base no tempo gasto para percorrer uma pequena parte do percurso. Para isso ele
recorre a uma formulação matemática definida a seguir.
Considerando o percurso AB, que determina o percurso total da maratona, o trecho AB’, que
determina um pequeno trecho deste percurso, e t o tempo para percorrer o trecho AB’, o cálculo
do tempo total T, estimado para percorrer o percurso total AB com base no tempo t, com uma
precisão de n termos, é dado pelo somatório:
T = t/2^0 + t/2^1 + t/2^2 + ... + t/2^(n-1)
Ajude o preparador físico implementando um programa que receba como entradas os valores de t e
n (ambos inteiros), calcule e imprima o valor de T. A saída precisa ser formatada com 4
casas decimais.'''

tempo = int (input('\nDigite o tempo AB´: '))
numero = int(input('\nDigite a distância AB´: '))

T = 0

for i in range(numero):
    T += tempo / 2 ** i

print(f'\nTempo total T = {T:.4f}\n')
