'''Utilizando a lista criada anteriormente, crie um outro método capaz de substituir um valor 
passado como parâmetro por 0. Utilize o mesmo método criado no Exercício 1 para imprimir a lista 
modificada. Exemplo: Entrada: valor 6 Saída: 1 2 3 4 5 0 7 8 9'''


class Armazenar:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.lista_valores = []

        for _ in range(0, capacidade):
            self.lista_valores.append(None)


    def preencher(self):
        for i in range(0, len(self.lista_valores)):
            self.lista_valores[i] = i + 1


    def trocar_numero(self, valor):
        for i in range(0, len(self.lista_valores)):
            if self.lista_valores[i] == valor:
                self.lista_valores[i] = 0


    def imprimir(self):
        print()

        for i in range(len(self.lista_valores)):
            print(f'{self.lista_valores[i]}', end=' ')

        print('\n')


dia = Armazenar(21)

dia.preencher()

dia.imprimir()

dia.trocar_numero(10)

dia.imprimir()
