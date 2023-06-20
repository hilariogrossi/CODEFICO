'''Segundo uma tabela médica, o peso ideal está relacionado com a altura e o sexo de uma pessoa. Implemente um programa que receba como entradas a altura
(número real) e o sexo (valor textual); a seguir ele calcula e imprime o peso ideal dessa pessoa, utilizando as seguintes fórmulas:

Para o sexo masculino: (72, 7 × H) − 58
Para o sexo feminino: (62, 1 × H) − 44, 7

Observações:

Considere que o usuário digitará uma das letras: ‘m’ para masculino ou ‘f’ para feminino.
Obtenha o peso ideal de acordo com o respectivo sexo e imprima o resultado com duas casas decimais.'''

H = float(input('Digite a altura: '))
sexo = input('Digite o sexo (M ou F): ').upper()

if sexo == 'M':
    peso = (72.7 * H) - 58
    print(f'O peso ideal é: {peso:.2f}!')
elif sexo == 'F':
    peso = (62.1 * H) - 44.7
    print(f'O peso ideal é: {peso:.2f}!')
else:
    print('A letra digitada não corresponde ao que se pede!')
