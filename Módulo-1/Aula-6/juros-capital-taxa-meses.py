# Descrição: Você foi contratado por uma empresa financeira que realiza empréstimos com cobrança de juros simples. O cálculo dos juros é realizado da seguinte
# forma: J = C × t × m, onde J é o valor dos juros devido, C é o capital emprestado, t é a taxa de juros do período e m é a quantidade de meses para quitação
# da dívida. A taxa de juros depende do capital emprestado: para valores menores ou iguais a R$ 10.000,00, a taxa de juros é de 10 % e acima R$ 10.000,00,
# a taxa de juros é de 7% ao mês (ou seja, t = 0,07). Implemente um programa que receba inicialmente o valor do capital total (T, em reais) que você possui para fazer empréstimos.
# Em seguida, você realizará empréstimos enquanto tiver capital total suficiente. A cada empréstimo realizado, você receberá duas entradas: C (em reais) e m (inteiro), e determinará
# a taxa de juros t, levando em consideração o valor do capital emprestado. Em seguida, calcule o valor de juros devido (J) e imprima a taxa de juros aplicada (valor percentual,
# com 0 casas decimais), o juros devido calculado (J, com 2 casas decimais) e o valor total da dívida (soma do capital emprestado e os juros devidos, também com 2 casas decimais).
# Após cada empréstimo, atualize seu capital total (T = T - C). O programa encerrará quando o valor do capital total T for insuficiente para fornecer o empréstimo solicitado C,
# e imprimirá uma mensagem de encerramento com o capital total final (com duas casas decimais). Nesse caso, o empréstimo será negado, o valor de m não será solicitado e o
# programa será encerrado.

T = float(input('\nEntre com o valor do capital total: R$ '))
C = float(input('\nEntre com o valor requerido do empréstimo: R$ '))

while C <= T:
    m = int(input('\nEntre com a quantidade de meses para pagamento do empréstimo: '))

    if C <= 10000 and m >= 1:
        TAXA = 0.1
        J = C * TAXA * m
    else:
        TAXA = 0.07
        J = C * TAXA * m
    
    T -= C

    print(f'\nTaxa de juros = {TAXA * 100:.0f} %\n\nValor dos Juros = R$ {J:.2f}\n\nValor total da dívida = R$ {J + C:.2f}')

    C = float(input('\nEntre com o valor requerido do empréstimo: R$ '))
    
print(f'\nO empréstimo será negado, o valor do capital final = R$ {T:.2f}\n')
