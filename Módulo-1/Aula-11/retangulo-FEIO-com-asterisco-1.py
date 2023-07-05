while True:
    imprimir = input('\nDeseja imprimir um retângulo? [S] Sim ou [N] Não: ').upper()

    if imprimir == 'N':
        print('\nOK! Saindodo programa...\n')
        break
    if imprimir != 'S':
        print('\nENTRADA INVÁLIDA! Informe se deseja imprimir um retângulo? [S] Sim ou [N] Não: ')
        continue
    a = int(input('\nInforme a altura do retângulo: '))
    l = int(input('\nInforme a largura do retângulo: '))

    while a <= 0 or l <= 0 or l <= 0:
        print('\nENTRADA INVÁLIDA!')
        a = int(input('\nInforme a altura do retângulo: '))
        l = int(input('\nInforme a largura do retângulo: '))

    aux = 0

    while aux < a:
        asterisco = '*'
        linha = asterisco * l
        print(f'\n{linha}')
        aux += 1
