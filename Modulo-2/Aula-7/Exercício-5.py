'''Implemente uma função que faça união de dois dicionários: d1 = {'a':1, 'b':2, 'c': 3}
d2 = {'b':10, 'd': 20, 'e': 30} resultado = unir_dicionario(d1,d2). Mander chaves iguais com os
dois valores. resultado = {'a': [1], 'b': [2, 10], 'c': [3], 'd': [20], 'e': [30]}'''


def unir_dicionarios_mantendo_chaves_duplas(dic1, dic2):
    resultado = {}

    for chave, valor in dic1.items():
        resultado[chave] = [valor]

    for chave, valor in dic2.items():
        if chave in resultado:
            resultado[chave].append(valor)
        else:
            resultado[chave] = [valor]

    return resultado


d1 = {'a':1, 'b':2, 'c': 3}
d2 = {'b':10, 'd': 20, 'e': 30}

resultado_final = unir_dicionarios_mantendo_chaves_duplas(d1, d2)

print(f'\nO resultado final mantendo chaves duplas ficou assim: {resultado_final}.\n')
