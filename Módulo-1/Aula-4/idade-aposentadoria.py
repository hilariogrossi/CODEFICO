# Aposentadoria

idade = int(input('Entre com a idade: '))
contribuição = float(input('Entre com o tempo de contribuição: '))

if idade >= 1 and contribuição >= 1:
  if idade >= 50 and contribuição >= 30 and idade + contribuição >= 90:
    print('Já pode se aposentar!')
  else:
    print('Não pode se aposentar!')
else:
  print('Dados de entrada inválidos. Saindo do programa...\n')
