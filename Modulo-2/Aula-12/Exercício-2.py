'''Monte uma classe para reunir informações sobre carros. Cada carro criado deverá conter informações
sobre a marca, modelo e ano do mesmo. Em seguida, crie um método que retora uma string contendo todas
essas informações do carro. Por fim, imprima a string retornada (marca, modelo e ano) no terminal.
Exemplo: Entrada: marca do carro: "Fiat" modelo do carro: "Uno" ano: 2002 Saída: "Fiat Uno (2002)"'''

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


    def retorna_string(self):
        return f'"{self.marca} {self.modelo} ({self.ano})"'


res = Carro('Fiat', 'Uno', 2022)

print(f'\n{res.retorna_string()}\n')
