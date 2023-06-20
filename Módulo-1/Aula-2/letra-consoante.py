# Implemente um Programa que verifique se uma letra digitada é vogal ou
# consoante.

# Dica: Identificar vogal é simples pois são apenas 5.
# As consoantes são todas as letras que não são iguais a essas 5.

letra = input('Digite uma letra do alfabeto: ').lower()

vogais = ['a', 'e', 'i', 'o', 'u']

if letra in vogais:
    print(f'A letra digitada "{letra}" é uma VOGAL!')
else:
    print(f'A letra digitada "{letra}" é uma CONSOANTE!')
