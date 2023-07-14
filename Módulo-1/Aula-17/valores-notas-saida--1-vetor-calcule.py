'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser
armazenado). Após esta entrada de dados, faça: Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro; Exiba todos os
valores na ordem inversa à que foram informados, um abaixo do outro; Calcule e mostre a soma dos
valores; Calcule e mostre a média dos valores; Calcule e mostre a quantidade de valores acima da
média calculada; Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem.'''

vetor = []
soma = media = 0

while True:
    notas = float(input('\nDigite a nota: '))

    if notas < 0:
        print('Encerrando o programa...')
        break

    vetor.append(notas)

print(f'\nA quantidade de valores lidos foram: {len(vetor)}')
print(f'\nOs valores na ordem em que foram informados: {vetor}')

for i in vetor[::-1]:
    print(f'\n{i}')

soma = sum(vetor)
print(f'\nA soma dos valores: {soma}')

media = sum(vetor) / len(vetor)
print(f'\nA média dos valores: {media}')


def contador(maior_media):
    cont = 0
    for i in maior_media:
        if i > media:
            cont += 1
    
    return cont

print(f'\nO(s) valor(es) acima da média calculada: {contador(vetor)}')


def menor_7(menor_7):
    cont = 0
    for i in menor_7:
        if i < 7:
            cont += 1

    return cont


print(f'\nO(s) valor(es) menores do que o valor 7: {menor_7(vetor)}\n')
