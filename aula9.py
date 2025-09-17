====================
CALCULADORA
====================

# Funções da calculadora
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

# Função para validar entrada de número
def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

# Função para mostrar o menu
def mostrar_menu():
    print("\n=== Calculadora Simples ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

# Programa principal
def main():
    while True:
        mostrar_menu()
        try:
            opcao = int(input("Escolha a opção: "))
        except ValueError:
            print("Opção inválida! Digite apenas números de 0 a 4.")
            continue

        if opcao == 0:
            print("Encerrando a calculadora...")
            break

        if opcao in [1, 2, 3, 4]:
            num1 = ler_numero("Digite o primeiro número: ")
            num2 = ler_numero("Digite o segundo número: ")

            if opcao == 1:
                print(f"Resultado: {somar(num1, num2)}")
            elif opcao == 2:
                print(f"Resultado: {subtrair(num1, num2)}")
            elif opcao == 3:
                print(f"Resultado: {multiplicar(num1, num2)}")
            elif opcao == 4:
                print(f"Resultado: {dividir(num1, num2)}")
        else:
            print("Opção inválida! Escolha entre 0 e 4.")


# Execução do programa
if __name__ == "__main__":
    main()
    

======================
FUNÇÕES LAMBDA
======================

# Operações usando lambdas
somar = lambda a, b: a + b
subtrair = lambda a, b: a - b
multiplicar = lambda a, b: a * b
dividir = lambda a, b: "Erro: divisão por zero!" if b == 0 else a / b

# Função para validar entrada de número
def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite um número válido.")
            continue

# Função para mostrar o menu
def mostrar_menu():
    print("\n=== Calculadora Simples ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

# Programa principal
def main():
    while True:
        mostrar_menu()
        try:
            opcao = int(input("Escolha a opção: "))
        except ValueError:
            print("Opção inválida! Digite apenas números de 0 a 4.")
            continue

        if opcao == 0:
            print("Encerrando a calculadora...")
            break

        if opcao in [1, 2, 3, 4]:
            num1 = ler_numero("Digite o primeiro número: ")
            num2 = ler_numero("Digite o segundo número: ")

            match opcao:
                case 1:
                    print(f"Resultado: {somar(num1, num2)}")
                case 2:
                    print(f"Resultado: {subtrair(num1, num2)}")
                case 3:
                    print(f"Resultado: {multiplicar(num1, num2)}")
                case 4:
                    print(f"Resultado: {dividir(num1, num2)}")
        else:
            print("Opção inválida! Escolha entre 0 e 4.")


# Execução do programa
if __name__ == "__main__":
    main()
