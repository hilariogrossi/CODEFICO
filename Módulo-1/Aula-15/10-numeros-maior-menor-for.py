'''Desenvolva um programa que receba como entrada 10 números digitados pelo usuário. Em seguida,
o programa deve calcular e exibir o menor e o maior valor dentre os números fornecidos.
O programa deve solicitar ao usuário que digite os números e, em seguida, realizar a comparação
para encontrar o menor e o maior valor. Por fim, exibirá os resultados encontrados. O programa deve
realizar as seguintes etapas:
1. Inicialize as variáveis menor_numero e maior_numero com valores extremos, como o maior número
possível e o menor número possível, respectivamente.
2. Crie um loop que irá iterar 10 vezes para ler os 10 números digitados pelo usuário.
3. Dentro do loop, solicite ao usuário que digite um número.
4. Verifique se o número digitado é menor que menor_numero ou se é maior que maior_numero. Se for, atualize o valor de menor_numero.
5. Exiba o menor número encontrado e o maior número encontrado.'''

menor_numero = maior_numero = 0

for i in range(10):
    numero_usuario = int(input(f'\nEntre com um {i + 1}° número para verificação: '))

    if i == 0:
        menor_numero = maior_numero = numero_usuario

    if  numero_usuario < menor_numero:
        menor_numero = numero_usuario
    elif numero_usuario > maior_numero:
        maior_numero = numero_usuario

print(f'\n\nO menor número digitado pelo usuário foi {menor_numero}.')
print(f'\nO maior número digitado pelo usuário foi {maior_numero}.\n')
