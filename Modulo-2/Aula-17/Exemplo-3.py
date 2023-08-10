# Inverte string

def inverte_string(s):
    if len(s) < 1:
        return s

    return s[-1] + inverte_string(s[:-1])


string = input('\nDigite a palavra a ser invertida: ')

res = inverte_string(string)

print(f'\nA palavra {string} invertida é {res}.\n')
