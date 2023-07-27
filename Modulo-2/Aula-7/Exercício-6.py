'''Implemente uma função que faça a inversao de um dicionário: d = {'a':1, 'b':2, 'c':2, 'd':3}
resultado = inverter_dicionario(d) # resultado = {1:['a'], 2:['b','c'], 3:['d']}'''


def inverter_dicionario(d):
    dicionario_invertido = {}

    for chave, valor in d.items():
        if valor in dicionario_invertido:
            dicionario_invertido[valor].append(chave)
        else:
            dicionario_invertido[valor] = [chave]

    return dicionario_invertido


dicionario = {'a':1, 'b':2, 'c':2, 'd':3}

resultado_final = inverter_dicionario(dicionario)

print(f'\nO resultado da inversão de chaves por valores é: {resultado_final}.\n')
