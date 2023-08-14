# Tempo de exercução de um algoritmo de inserção

from random import randint
from datetime import datetime


class Ordenacao:
    def __init__(self):
        self.lista = []
        self.tamanho = 0
        self.tempo = 0.0


    def criar_array_aleatorio(self, tamanho):
        self.tamanho = tamanho

        while len(self.lista) != self.tamanho:
            elemento = randint(0, 100000)
            self.lista.append(elemento)


    def insercao(self):
        for i in range(1, len(self.lista)):
            aux = self.lista[i]
            j = i - 1

            while j >= 0 and aux < self.lista[j]:
                self.lista[j + 1] = self.lista[j]
                j -= 1

            self.lista[j + 1] = aux


    def medir_tempo_inserção(self):
        tempo_inicial = datetime.now()
        self.insercao()
        tempo_final = datetime.now()

        self.tempo = tempo_final - tempo_inicial


    def final(self):
        tamanho = int(input('\nDigite o tamanho da lista: '))
        self.criar_array_aleatorio(tamanho)

        print(f'\nLista sem ordenação: {self.lista}')

        self.medir_tempo_inserção()

        print(f'\nLista ordenada: {self.lista}')

        print(f'\nTempo de inserção: {self.tempo}\n')




lista = Ordenacao()

lista.final()
