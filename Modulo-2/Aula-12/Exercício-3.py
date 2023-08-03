'''Crie uma classe com um contador. Sua classe não deve receber nenhum valor por parâmetro, mas deve
definir um atributo valor como 15. Em seguida, crie um método capaz de incrementar e outro para 
decrementar em 1 esse valor. No fim, imprima a o dia de seu nascimento, através do valor desse 
contador. Dica: incremente e decremente o valor quantas vezes for necessário até alcançar o dia de 
seu aniversário. Exemplo: Entrada: Saída: "8"'''

class Contador:
    def __init__(self):
        self.valor = 15


    def incrementar(self):
        self.valor += 1


    def decrementar(self):
        self.valor -= 1


contador = Contador()

while contador.valor != 21:
    contador.incrementar()

print(contador.valor)
