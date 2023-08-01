'''Escreva um programa que leia o conteúdo de um arquivo de texto chamado "notas.txt", onde cada linha contém o nome de um aluno seguido de sua nota. Calcule a média
das notas e exiba na tela o nome do aluno com a nota mais alta. Exemplo de entrada (conteúdo do arquivo "notas.txt"):
João, 8.5
Maria, 9.0
Pedro, 7.5
Ana, 9.5
Exemplo de saída: A média das notas é: 8.62
O aluno com a nota mais alta é: Ana

Nesse exemplo, o arquivo "notas.txt" contém o nome de cada aluno seguido de sua respectiva nota em cada linha. O programa lê o conteúdo do arquivo, calcula a média das notas 
e exibe a média na tela. Além disso, o programa identifica o aluno com a nota mais alta e exibe o nome desse aluno.
Você pode adicionar mais linhas ao arquivo "notas.txt" com o nome e a nota de outros alunos para testar o programa.'''

cont = int(input('\nDigite a quantidade de alunos: '))

if cont == 0:
    print('\nO primeiro número NÃO pode ser ZERO (0). Saindo do programa...\n')
    exit()

elif cont < 0:
    print(f'\nA quantidade de alunos não pode ser menor do que zero. Você digitou: {cont}.\n')
    exit()

else:
    while cont > 0:
        nome_notas = input('\nDigite o nome de um aluno seguido de sua nota [nome, nota]: ')
        with open("notas.txt", 'a') as arquivo:
            arquivo.write(f'{nome_notas}\n')
        cont -= 1

    if cont == 0:
        with open('notas.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        soma = quantidade = 0

        for linha in linhas:
            partes = linha.split(', ')
            nota = partes[1].replace('\n', '')
            nota = float(nota)
            soma += nota
            quantidade += 1

        media = soma / quantidade

        nota_maxima = float('-inf')
        nota_minima = float('inf')
        aluno_maior_nota = ''
        aluno_menor_nota = ''

        for linha in linhas:
            partes = linha.split(', ')
            aluno = partes[0]
            nota = partes[1].replace('\n', '')
            nota = float(nota)

            if nota > nota_maxima:
                nota_maxima = nota
                aluno_maior_nota = aluno

            elif nota < nota_minima:
                nota_minima = nota
                aluno_menor_nota = aluno

    print(f"\nA média das notas é : {media:.2f} ")
    print(f"\nO Aluno com a nota mais alta: {aluno_maior_nota}")
    print("\nAluno com menor nota:", aluno_menor_nota)
