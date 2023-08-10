# Retorna maior valor de uma lista


def max_lista(lista):
    if len(lista) == 1:
        return lista[0]

    else:
        aux = max_lista(lista[:-1])

        if aux > lista[-1]:
            return aux

        else:
            return lista[-1]


l  = [1, 76, 4, 7, 11, 44, 26, 5, 2]
res = max_lista(l)

print(f'\nO maior valor da lista {l} é ==> {res}.\n')
