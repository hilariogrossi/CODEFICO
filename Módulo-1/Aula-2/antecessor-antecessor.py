# Codifique um programa que leia um número inteiro qualquer e imprima o seu sucessor e seu antecessor.

numero = int(input('Digite um número inteiro: '))

sucessor = numero + 1
antecessor = numero - 1

print(f'O antecessor do número "{numero}" é {antecessor} e seu sucessor é {sucessor}.')
