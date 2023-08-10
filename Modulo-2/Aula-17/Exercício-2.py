# Collatz (3n + 1)

def collatz(n):
    lista = [n]

    if n == 1:
        return lista

    if n % 2 == 0:
        return lista + collatz(n // 2)

    return lista + collatz(3 * n + 1)


numero = int(input('\nEntre com o número para calcular o Collatz: '))
print(f'\nA lista para calcular o Collatz do {numero} é: {collatz(numero)}\n')
