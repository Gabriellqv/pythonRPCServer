# type: ignore[assignment]
import rpyc  # Biblioteca para Python RPC
from rpyc.utils.server import ThreadedServer

class MyService(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_calculate_imc(self, weight, height):
        # Calcula o IMC e retorna o resultado.
        imc = weight / (height ** 2)
        return imc

    def exposed_calculate_quadraticEquation(self, a, b, c):
        import math

        # Verifica as condicoes e calculas as raizes
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            return x1, x2
        elif discriminant == 0:
            # Raiz real única (raízes iguais)
            x1 = -b / (2*a)
            return x1
        else:
            # Não há raízes reais (raízes complexas)
            real_part = -b / (2*a)
            imaginary_part = math.sqrt(-discriminant) / (2*a)
            return real_part + imaginary_part * 1j, real_part - imaginary_part * 1j

    def exposed_check_palindrome(self, word):

        # Converte a palavra em minuscula e remove os espacos em branco da palavra para verificacao de palindromo.
        word = word.lower().replace(" ", "")
        return word == word[::-1]

# Verifica se o script está sendo executado como um programa principal
if __name__ == "__main__":
    try:
        server = ThreadedServer(MyService, hostname='0.0.0.0', port=18812)
        print('Servidor online')
        # Inicia o servidor, permitindo que ele comece a aceitar conexões de clientes
        server.start()
        # Captura uma exceção de interrupção do teclado para poder encerrar o servidor.
    except KeyboardInterrupt:
        print('Servidor encerrado')