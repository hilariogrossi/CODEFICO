# Palíndromo com função recursiva


def verificar_palindromo(string):
    string = string.upper()
    if len(string) <= 0:
        print('A string está vazia. Tente novamente com uma palavra ou frase...')

    elif len(string) == 1:
        return True

    if string[0] != string[-1]:
        return False

    return verificar_palindromo(string[1:-1])


palavra = input('\nEntre com a palvra ou frase: ')

res = verificar_palindromo(palavra)

print(res)
