# Árvore Binária


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


    def mostra_no(self):
        print(self.valor)


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None


    def insere(self, elemento):
        novo_no = No(elemento)

        if self.raiz is None:
            self.raiz = novo_no

        else:
            atual = self.raiz

            while True:
                pai = atual

                if elemento < atual.valor:
                    atual = atual.esquerda

                    if atual is None:
                        pai.esquerda = novo_no
                        return

                else:
                    atual = atual.direita

                    if atual is None:
                        pai.direita = novo_no
                        return


    def pre_ordem(self, no):
        if no is not None:
            print(f'{no.valor}', end=' ')
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)


    def ordem_central(self, no):
        if no is not None:
            self.ordem_central(no.esquerda)
            print(f'{no.valor}', end=' ')
            self.ordem_central(no.direita)


    def pos_ordem(self, no):
        if no is not None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(f'{no.valor}', end=' ')




arvore = ArvoreBinaria()

elementos = [5, 2, 8, 1, 3, 7, 9, 4, 6, 10]

for elemento in elementos:
    arvore.insere(elemento)

print('\nCaminhamento Pré-Ordem:')
arvore.pre_ordem(arvore.raiz)
print('\n')

print('\nCaminhamento Ordem Central:')
arvore.ordem_central(arvore.raiz)
print('\n')

print('\nCaminhamento Pós-Ordem:')
arvore.pos_ordem(arvore.raiz)
print('\n')
