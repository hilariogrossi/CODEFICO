'''Utilizando a classe Aluno criada anteriormente, instancie um objeto e use os métodos da classe 
para inserir 5 alunos. Além disso, crie um método para imprimir todos os nomes dos alunos e escreva 
uma mensagem de parabéns para o aluno que tenha tirado a melhor nota. OBS: Caso mais de um aluno 
tenham tirado a melhor nota, escreva a mensagem para todos eles. Exemplo: Entrada:
aluno1: Vitor Jose, 6
aluno2: Pedro Silva, 7
aluno3: Maria Clara, 9
aluno4: Ian Ferreira, 4
aluno5: Emanuelle Melo, 10

Saída:

Turma:
Vitor Jose
Pedro Silva
Maria Clara
Ian Ferreira
Emanuelle Melo, parabéns!!!'''


class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota


class salaDeAula:
    def __init__(self):
        self.turma = []

    def novato(self, aluno):
        self.turma.append(aluno)

    def chamada(self):
        maior = 0

        for i in range(0, len(self.turma)):
            if self.turma[i].nota > maior:
                maior = self.turma[i].nota

        for i in range(0, len(self.turma)):
            if self.turma[i].nota == maior:
                print(
                    f"\n{self.turma[i].nome} parabéns pela nota {self.turma[i].nota}!!!")
            else:
                print(f"\n{self.turma[i].nome}")

        print('\n')


sala = salaDeAula()

aluno1 = Aluno('Vitor Jose', 6)
sala.novato(aluno1)

aluno2 = Aluno('Pedro Silva', 7)
sala.novato(aluno2)

aluno3 = Aluno('Maria Clara', 9)
sala.novato(aluno3)

aluno4 = Aluno('Ian Ferreira', 4)
sala.novato(aluno4)

aluno5 = Aluno('Emanuelle Melo', 10)
sala.novato(aluno5)

sala.chamada()
