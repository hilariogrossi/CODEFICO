# Contador de dígitos


def contar_digitos(n):
    if n < 10:
        return 1

    return 1 + contar_digitos(n // 10)


numero = int(input('\nEntre com o número inteiro para contar seus dígitos: '))

res = contar_digitos(numero)

print(f'\nO número {numero} contém {res} dígitos.\n')
