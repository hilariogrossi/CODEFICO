'''Árvore Binária'''


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None


    def inserir(self, elemento):
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


    def encontra_no_minimo(self, no_atual):
        while no_atual.esquerda is not None:
            no_atual = no_atual.esquerda


    def remover(self, no, elemento):
        if no is None:
            return no

        if elemento < no.valor:
            no.esquerda = self.remover(no.esquerda, elemento)

        elif elemento > no.valor:
            no.direita = self.remover(no.direita, elemento)

        else:
            if no.direita is None:
                return no.esquerda

            elif no.esquerda is None:
                return no.direita

            sub_minimo = self.encontra_no_minimo(no.direita)
            no.valor = sub_minimo.valor
            no.direita = self.remover(no.direita, sub_minimo.valor)

        return no



arvore = ArvoreBinaria()

elementos = [8, 4, 2, 6, 1, 3, 5, 7, 12, 10, 14, 9, 11, 13, 15]

for elemento in elementos:
    arvore.inserir(elemento)

print('\nEncaminhamento Pré-Ordem')
arvore.pre_ordem(arvore.raiz)
print('\n')

print('\nEncaminhamento Ordem Central')
arvore.ordem_central(arvore.raiz)
print('\n')

print('\nEncaminhamento Pós-Ordem')
arvore.pos_ordem(arvore.raiz)
print('\n')

elemento_remover = int(input('\nQual elemento deseja remover? '))
print(f'\nRemovendo o elemento {elemento_remover}.')

arvore.remover(arvore.raiz, elemento_remover)

print(f'\nEncaminhamento Ordem Central APÓS REMOÇÃO do elemento {elemento_remover}.')
arvore.ordem_central(arvore.raiz)
print('\n')
