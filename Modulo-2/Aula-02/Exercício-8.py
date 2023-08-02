'''Desenvolva um programa em Python que registre as vendas de uma loja em um arquivo de texto. O programa deve permitir que o usuário adicione informações sobre cada venda,
como o nome do produto, a quantidade vendida e o preço unitário. O programa deve seguir as seguintes etapas:
- O programa deve solicitar ao usuário que digite o nome do arquivo onde deseja registrar as vendas.
    Exemplo de entrada: Digite o nome do arquivo: vendas.txt
- Em seguida, o programa deve solicitar ao usuário que digite as informações sobre a venda, incluindo o nome do produto, a quantidade vendida e o preço unitário.
  Exemplo de entrada: Digite o nome do produto: Camiseta - Digite a quantidade vendida: 10 - Digite o preço unitário: 29.99 
- O programa deve abrir o arquivo no modo de anexação ("a") para adicionar as informações da venda ao final do arquivo.
- As informações da venda devem estar separadas com por ponto e virgula(;) no arquivo, como no exemplo do arquivo de vendas.txt. Após a gravação das informações, o programa 
deve exibir a mensagem - Exemplo de saída: "Venda registrada com sucesso!". Exemplo de como deve ficar o arquivo vendas.txt Camiseta;10;29.99'''
'''

nome_arquivo = input('\nEntre com o nome do arquivo que deseja abrir: ')

while True:
    nome_produto = input('\nEntre com o nome do produto [# para sair]: ')
    if nome_produto == '#':
        print('\nSaindo do programa...\n')
        break
    quantidade_produto = int(input('\nEntre com a quantidade vendida: '))
    preco = float(input('\nEnte com o preço unitário: '))

    with open('Aula-2/' + nome_arquivo + '.txt', 'a') as arquivo:
        venda = f'{nome_produto}; {quantidade_produto}; {preco}\n'
        arquivo.write(venda)

    print('\n"Venda registrada com sucesso!"\n')
