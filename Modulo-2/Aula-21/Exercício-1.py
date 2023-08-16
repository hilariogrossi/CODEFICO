# QuickSort

from random import randint
from datetime import datetime


class Quicksort:
    def __init__(self):
        self.array = []
        self.tamanho = 0 # Tamanho da lista
        self.tempo = 0.0


    def partition(self, indice_low, indice_high):
        i = indice_low
        j = indice_high

        pivot_index = (indice_low + indice_high) // 2
        pivot = self.array[pivot_index]

        while True:
            while self.array[i] < pivot:
                i += 1

            while pivot < self.array[j]:
                j -= 1

            if i >= j:
                break

            else:
                self.array[i], self.array[j] = self.array[j], self.array[i]


        return i


    def quicksort(self, indice_low, indice_high):
        if indice_low < indice_high:
            pivot_position = self.partition(indice_low, indice_high)

            self.quicksort(indice_low, pivot_position - 1)
            self.quicksort(pivot_position + 1, indice_high)


    def sort(self):
        self.quicksort(0, self.tamanho - 1)


    def criar_array_aleatório(self, tamanho):
            self.tamanho = tamanho

            self.array = [randint(0, 100000) for _ in range(self.tamanho)]

            '''for _ in range(self.tamanho):
                elemento = randint(0, 100000)
                self.array.append(elemento)'''


    def medir_tempo_quick(self):
        tempo_inicial = datetime.now()
        self.sort()
        tempo_final = datetime.now()

        self.tempo = tempo_final - tempo_inicial


    def final(self):
        tamanho = int(input('\nDigite o tamanho da lista: '))
        self.criar_array_aleatório(tamanho)

        print(f'\nA lista original: {self.array}')

        self.medir_tempo_quick()

        print(f'\nA lista ordenada: {self.array}')

        print(f'\nO tempo de execução do Quicksort foi: {self.tempo} (horas:minutos:segundos.microssegundos).\n')



ordenacao_quicksort = Quicksort()

ordenacao_quicksort.final()
