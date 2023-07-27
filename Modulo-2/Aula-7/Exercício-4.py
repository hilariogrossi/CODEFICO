'''Implemente uma função que faça união de dois dicionários: d1 = {'a':1, 'b':2, 'c': 3}
d2 = {'b':10, 'd': 20, 'e': 30} resultado = unir_dicionario(d1,d2)
# resultado = {'a':1, 'b':2, 'c':3, 'd': 20, 'e': 30}'''

def unir_dicionarios(dic1, dic2):
    resultado = dic1.copy()
    resultado.update(dic2)

    return resultado


d1 = {'a':1, 'b':2, 'c': 3}
d2 = {'b':10, 'd': 20, 'e': 30}

resultado_final = unir_dicionarios(d1, d2)

print(f'\nO dicionário final ficou assim: {resultado_final}.\n')
