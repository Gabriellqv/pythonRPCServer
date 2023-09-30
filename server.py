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
        imc = weight / (height**2)
        # Com o IMC calculado, esta parte classifica e apresenta o estado de saúde do usuário.
        if imc < 16:
            estate = "Magreza grave. Procure um médico ou nutricionista."
        elif imc < 17:
            estate = "Seu estado é de Magreza moderada Precisa rever sua alimentação."
        elif imc < 18.5:
            estate = "Seu estado é de Magreza leve Precisa rever sua alimentação."
        elif imc < 25:
            estate = "Você está Saudável."
        elif imc < 30:
            estate = "Seu estado é de Sobrepeso Precisa rever sua alimentação."
        elif imc < 35:
            estate = (
                "Seu estado é de Obesidade Grau I Procure um médico ou nutricionista."
            )
        elif imc < 40:
            estate = "Seu estado é de Obesidade Grau II (severa) Procure um médico ou nutricionista."
        else:
            estate = "Seu estado é de Obesidade Grau III (mórbida) Procure um médico ou nutricionista."

        return imc, estate

    def exposed_calculate_quadraticEquation(self, a, b, c):
        import math

        # Verifica as condicoes e calcula as raizes
        discriminant = b**2 - 4 * a * c
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return x1, x2
        elif discriminant == 0:
            # Raiz real única (raizes iguais)
            x1 = -b / (2 * a)
            return x1
        else:
            # Não há raízes reais (raizes complexas)
            real_part = -b / (2 * a)
            imaginary_part = math.sqrt(-discriminant) / (2 * a)
            return real_part + imaginary_part * 1j, real_part - imaginary_part * 1j

    def exposed_check_palindrome(self, word):

        # Converte a palavra em minuscula e remove os espacos em branco da palavra para verificacao de palindromo.
        word = word.lower().replace(" ", "")
        return word == word[::-1]


# Verifica se o script está sendo executado como um programa principal
if __name__ == "__main__":
    try:
        server = ThreadedServer(MyService, hostname="0.0.0.0", port=18812)
        print("Servidor online")
        # Inicia o servidor, permitindo que ele comece a aceitar conexões de clientes
        server.start()
        # Captura uma exceção de interrupção do teclado para poder encerrar o servidor.
    except KeyboardInterrupt:
        print("Servidor encerrado")