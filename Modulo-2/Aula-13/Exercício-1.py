'''Uma lista é, resumidamente, uma classe que contém um vetor (array) de dados. Esses dados podem 
ser inteiros (1, 2, 3...) ou caracteres ("a", "b", "c"...) como de costume, mas também podem ser 
formados por uma outra classe, como a classe de Alunos que havíamos criado. Lembrando: Uma classe é 
formada por atributos e métodos. Os atributos são cada membro que compõe uma classe. Normalmente, 
são definidos no metódo __init__(). Já os metódos são blocos de código que analizam e/ou modificam 
os atributos criados. Exercício 1: Monte uma lista capaz de armazenar uma certa quantidade de 
valores inteiros em sequência, começando do 1 e indo até a data do seu aniversário. Em seguida, crie
um método capaz de imprimir toda essa sequência, do primeiro ao último valor.
Exemplo: Entrada: dia do aniversário : 9 Saída: 1 2 3 4 5 6 7 8 9 OBS: Os valores podem ficar cada um em uma linha.'''


class Armazenar:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.lista_valores = []

        for _ in range(0, capacidade):
            self.lista_valores.append(None)


    def preencher(self):
        for i in range(0, len(self.lista_valores)):
            self.lista_valores[i] = i + 1


    def imprimir(self):
        print()

        for i in range(len(self.lista_valores)):
            print(f'{i + 1}', end=' ')

        print('\n')


dia = Armazenar(21)

dia.preencher()

dia.imprimir()
