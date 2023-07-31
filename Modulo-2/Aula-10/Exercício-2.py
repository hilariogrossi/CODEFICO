'''Qual a ordem de complexidade do programa abaixo, em relação ao tamanho n da entrada, se considerarmos o número de comparações como medida de complexidade?'''


def f(a, tam):
    print()
    print("a:", a)
    for i in range(tam):
        print("teste")
        if i % 2 == 0:
            a[i] = i


def g(a, tam):
    print()
    for i in range(tam):
        if i % 2 == 0:
            print(a[i], end=" ")


def main():
    quant = int(input("Informe a quantidade de itens: "))
    a = [0] * quant  # Inicializa uma lista de tamanho 'quant' preenchida com zeros
    f(a, quant)
    g(a, quant)


main()

# # f(n) = 4n ou f(4) = 4 * tamanho vezes
