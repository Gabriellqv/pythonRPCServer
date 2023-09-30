import rpyc

# Exibe um menu de opções para o usuário.
def menu():
    print("Escolha uma opção:")
    print("1 - Calcular o IMC")
    print("2 - Resolver uma equação de segundo grau")
    print("3 - Verificar se uma palavra é um palíndromo")
    print("4 - Sair")
    print("\n")


def main():
    try:
        # Conecta ao servidor RPC
        conn = rpyc.connect(
            "localhost", 18812
        )  # Substitua 'localhost' pelo endereço do servidor, se necessário

        while True:
            menu()  # Chama a função menu
            choice = input("Digite o número da opção desejada: ")

            if choice == "1":
                # Chama o método calculate_imc do servidor
                print("----------------------------------")
                print("Calculadora de IMC")
                print("----------------------------------")

                # Solicita e armazena o peso e a altura do usuário para realizar o cálculo.
                try:
                    weight = float(input("Digite seu peso em quilogramas (ex: 70): "))
                    height = float(input("Digite sua altura em metros (ex: 1.75): "))
                except ValueError:
                    print("Erro: Insira valores numéricos válidos para peso e altura.")
                    continue  # Volte ao menu

                result_imc = conn.root.exposed_calculate_imc(weight, height)
                imc, estate = result_imc
                print("----------------------------------")
                print("Vamos calcular seu IMC")
                print("----------------------------------")
                # Apresenta o resultado do IMC
                print(f"Seu IMC é: {imc:.2f}")
                # Apresenta o resultado do estado de saude do usuario
                print(estate + "\n")

            elif choice == "2":
                # Chama o método calculate_quadraticEquation do servidor
                print("----------------------------------")
                print("Calcular equação de segundo grau")
                print("----------------------------------")

                # Solicitar os coeficientes da equação de segundo grau ao usuário (ax^2 + bx + c = 0)
                try:
                    a = float(
                        input("Digite o valor do coeficiente 'a' (não pode ser zero): ")
                    )
                    while a == 0:
                        print(
                            "***********************************************************"
                        )
                        print(
                            "O coeficiente 'a' não pode ser zero. Tente um valor válido."
                        )
                        print(
                            "***********************************************************"
                        )
                        a = float(
                            input(
                                "Digite o valor do coeficiente 'a' (não pode ser zero): "
                            )
                        )
                    b = float(input("Digite o valor do coeficiente 'b': "))
                    c = float(input("Digite o valor do coeficiente 'c': "))
                except ValueError:
                    print(
                        "Erro: Insira valores numéricos válidos para os coeficientes."
                    )
                    continue  # Volte ao menu

                print("----------------------------------")

                # Apresenta o resultado da equacao
                result = conn.root.exposed_calculate_quadraticEquation(a, b, c)
                if isinstance(result, tuple):
                    print(f"As raízes são x1 = {result[0]} e x2 = {result[1]}\n")
                else:
                    if isinstance(result, (float, int)):
                        print(f"A raiz única é x = {result}\n")
                    else:
                        real_part = result[0].real
                        imaginary_part = result[0].imag
                        print(
                            f"As raízes são complexas: x1 = {real_part} + {imaginary_part}i e x2 = {real_part} - {imaginary_part}i\n"
                        )

            elif choice == "3":
                # Chama o método check_palindrome do servidor
                print("----------------------------------")
                print("Verificador de palíndromo")
                print("----------------------------------")

                # Solicita e armazena a palavra inserida pelo usuário.
                word = input("Digite uma palavra para verificar se é um palíndromo: ")
                is_palindrome = conn.root.exposed_check_palindrome(word)
                # Verifica se a palavra é igual à sua versão invertida.
                if is_palindrome:
                    print(f"{word} é um palíndromo.\n")
                else:
                    print(f"{word} não é um palíndromo.\n")

            elif choice == "4":
                print("Saindo do cliente.\n")
                break  # Sair do loop e encerrar o programa

            else:
                print("Opção inválida. Escolha uma opção válida.")

    except ConnectionRefusedError:
        print(
            "Erro: Não foi possível conectar ao servidor. Verifique se o servidor está em execução."
        )
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    main()