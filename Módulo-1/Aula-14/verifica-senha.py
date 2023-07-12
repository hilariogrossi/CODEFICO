'''Crie uma função “verificar_senha” no qual retorna true caso a senha inserida for correta e false
caso o contrário. Logo após elabore um “mini-sistema” de checar a senha inserida, onde o usuário
tem 3 tentativas de senha e caso esse número seja ultrapassado o programa é encerrado.
DICA: A senha correta será definida por você.'''


def verificar_senha(senha_usuario):
    senha_base = '12345'

    if senha_usuario == senha_base:
        return True
    else:
        return False


tentativa = 3

while tentativa > 0:
    senha = input('\nEntre com a senha: ')

    verifica = verificar_senha(senha)

    if verifica:
        print('\nSENHA CORRETA!\n')
        break
    else:
        tentativa -= 1
        print(f'\nVocê ainda tem {tentativa} tentativa(s).')

if tentativa == 0:
    print('\nSENHA INCORRETA. Você excedeu as 3 tentantivas possíveis.\n')
