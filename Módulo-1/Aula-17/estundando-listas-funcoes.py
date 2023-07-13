''' Faça um programa que solicite ao usuário a entrada de uma lista de valores reais.
Seu programa deve fazer com que esta entrada se transforme em um vetor de números
reais e a seguir fazer uma série de operações, sempre imprimindo o resultado após
a operação:
1. Imprimir a quantidade de elementos na lista, o maior preço, o menor preço e a soma de todos;
2. Inverter a ordem dos preços na lista;
3. Ordenar os preços em ordem crescente;
4. Inserir o valor 1,00 na posição 0 da lista, movendo os elementos para as próximas posições;
5. Inserir o valor 50,00 ao final da lista;
6. Remover o elemento que está na posição 0;
7. Remover um item de valor 50,00;
8. Replicar a lista para que ela tenha o dobro do tamanho e os valores sejam replicados.
(Conceito utilizado: métodos especiais para listas)
lista = 5.8, 10.00, 8.5, 4.5, 3.2, 6.5, 3.5, 6.4'''

lista = input('\nEntre com uma lista de valores reais: ').split(', ')
vetor = []

for i in range(len(lista)):
    vetor.append(float(lista[i]))

print(f'\nA lista possui a quantidade de {len(vetor)} elementos.')
print(f'\nO maior preço da lista é: R$ {max(vetor):.2f}')
print(f'\nO menor preço da lista é: R$ {min(vetor):.2f}')
print(f'\nA ordem invertida da lista é: R$ {str(vetor[::-1])}')

vetor.insert(0, 1.00)
print(f'\nInserindo o valor 1,00 na posição 0 lista: R$ {vetor}')

vetor.append(50.00)
print(f'\nInserindo o valor 50,00 no final da lista: R$ {vetor}')

vetor.pop(0)
print(f'\nRemover o elemento que está na posição 0 da lista: R$ {vetor}')

vetor.remove(50.00)
print(f'\nRemover o elemento que está na posição 0 da lista: R$ {vetor}')

print(f'\nRemover o elemento que está na posição 0 da lista: R$ {vetor * 2}\n')
