'''Uma escola quer acompanhar o crescimento dos alunos. Para isso, deseja armazenar a média de 
tamanho das turmas, possibilitando acompanhar o crescimento médio ao longo dos anos. Crie um 
programa que receba uma lista de tuplas, onde cada tupla contém o nome e a altura de um aluno. O 
programa deve retornar a altura média de todos os alunos.
Passo 1: Inserir o número alunos. Passo 2: Crie um loop para registrar o nome e tamanho do aluno em 
uma tupla. Passo 3: Criar um loop somar as alturas. Passo 4: Calcular a média.
Entrada: Digite o numero de alunos: 2
Digite o nome:Roberto Digite a altura:1.55
Digite o nome:Laura Digite a altura:1.62
Saída: Média das alturas: 1.58'''

numero_alunos = int(input('\nEntre com o número de alunos a serem analisados: '))
lista = []

for i in range(numero_alunos):
    tupla = []
    nome_aluno = input(f'\nDigite o nome do {i + 1}° aluno: ')
    altura_aluno = float(input(f'\nDigite a altura do {i + 1}° aluno: '))

    tupla.append(nome_aluno)
    tupla.append(altura_aluno)

    lista.append(tuple(tupla))

soma = media = 0

for i in range(numero_alunos):
    soma += lista[i][1]

media = soma / numero_alunos

print(f'\nA média da altura dos alunos é {media:.2f}\n')
