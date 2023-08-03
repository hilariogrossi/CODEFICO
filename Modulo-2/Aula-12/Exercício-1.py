'''Monte uma classe capaz de analisar se um aluno foi aprovado ou não em certa matéria. Cada aluno
deve possuir um nome e uma nota, passados como parâmetro na inicialização. Já a análise da nota 
sobre a média deve ser feita em um método, que recebe como parâmetro a nota referente a média 
daquela matéria. Caso a nota for maior ou igual a média, deve ser impresso uma mensagem dizendo que
o aluno foi aprovado. Caso contrário, uma mensagem dizendo que ele foi reprovado.
Exemplo: Entrada: nome do aluno: "Vitor" nota do aluno: 5 media na materia: 6
Saída: "Reprovado!"'''

class Analisar():
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota


    def aprovado_reprovado(self, media = 6):
        if self.nota >= media:
            print(f'\nO aluno {self.nome} foi aprovado!\n')

        else:
            print(f'\nO aluno {self.nome} foi reprovado!\n')


resposta = Analisar('Hilário', 8.5)

resposta.aprovado_reprovado()
