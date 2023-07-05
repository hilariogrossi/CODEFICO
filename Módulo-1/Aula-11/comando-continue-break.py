'''Para que serve o comando continue? Explique com suas palavras, e escreva um código que exemplifica sua explicação:
Serve para que um determinado comando do programa continue sem que o resto do programa seja afetado.'''

num1 = int(input("\nDigite um número inteiro: "))
num2 = int(input("\nDigite outro número inteiro: "))

cont = num1

while True:
    if cont % num1 == 0 and cont % num2 == 0:
        break
    #elif cont % num1 != 0 and cont % num2 != 0:
    #   continue
    else:
        cont += 1

print(f'\nO MMC de {num1} e {num2} é: {cont}\n')
