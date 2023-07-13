'''A CEMIG está treinando um novo funcionário para realizar as leituras de consumo residencial
de energia. Esse funcionário percorreu um roteiro pré-estabelecido e registrou o consumo das
residências. Outro funcionário, mais experiente, veio logo atrás fazendo a leitura das mesmas
residências, na mesma ordem. Os resultados obtidos pelos dois foram armazenados em dois
vetores, um para cada funcionário, e são fornecidos através de duas entradas de dados
pelo usuário.
Escreva um programa para calcular os valores absolutos das diferenças entre as leituras dos
dois funcionários e armazená-las em outro vetor, determinando também a média dos valores
armazenados no novo vetor e imprimindo os resultados na tela.
(Conceito utilizado: Entrada como listas e comparação de duas listas)'''

entrada_1 = input('\nEntre com a primeira lista (Somente números): ')
entrada_2 = input('\nEntre com a segunda lista (Somente números): ')

vetor_1 = list(map(int, entrada_1.split()))
vetor_2 = list(map(int, entrada_2.split()))

vetor_3 = [abs(a - b) for a, b in zip(vetor_1, vetor_2)]
soma = sum(vetor_3)
media = soma / len(vetor_3)

print('\nValores absolutos:', end=' ')
print(*vetor_3, sep=', ', end=', ')
print(f'\n\nMédia das diferenças absolutas: {media:.3f}\n')
