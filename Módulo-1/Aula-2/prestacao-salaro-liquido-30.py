# Empréstimo no qual o salário líquido que vale. No salário tem um desconto do INSS de 9% e esse empréstimo não poderá exceder 30% do salário liquído.

salario = float(input('Digite o seu salário: '))

salario_liquido = salario - (salario * 0.09)
trinta_porcento_salario = salario_liquido * 0.30

prestacao = float(input('Qual o valor da prestação que deseja pagar? '))

if prestacao <= trinta_porcento_salario:
    print('O empréstimo pode ser concedido!')
else:
    print('O empréstimo NÃO pode ser concedido.')
