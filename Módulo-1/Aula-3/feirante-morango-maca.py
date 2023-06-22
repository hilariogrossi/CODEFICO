# A feirante está vendendo frutas com os seguintes preços:
# Morango até 5 Kg R$ 2,50 por Kg e acima de 5 Kg R$ 2,20
# Maça até 5 Kg 1,80 por Kg e acima de 5 Kg 1,50
# Implemente um programa para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de
# maçãs adquiridas, ambos números reais, e escrever o valor a ser pago pelo cliente (com precisão
# de duas casas decimais). Se o cliente fornecer pelo menos uma das quantidades menor do que
# 0 (zero), a mensagem "Entrada inválida" deve ser exibida no terminal.

morango = float(input('Entre com a quantidade de morango em Kg: '))
maca = float(input('Entre com a quantidade de maçã em Kg: '))

if morango < 0 or maca < 0:
    print('Entrada Inválida!')
else:
    if morango < 5 and maca < 5:
        valor = morango * 2.5 + maca * 2.2
    elif morango >= 5 and maca < 5:
        valor = morango * 1.8 + maca * 2.2
    elif morango < 5 and maca >= 5:
        valor = morango * 2.5 + maca * 1.5
    else:
        valor = morango * 1.8 + maca * 1.5
    print(f'O valor total da compra é de R$ {valor:.2f}!')
