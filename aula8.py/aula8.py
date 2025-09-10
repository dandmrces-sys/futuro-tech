
while True:
    menu = int(input('''
    --- CALCULADORA ---
    1. Soma
    2. Subtração
    3. Multiplicação
    4. Divisão

   '''))
    
    if menu == 1:
        num1 = int (input('Digite um número: '))
        num2 = int (input('Digite outro número: '))
        resultado = num1 + num2
        print("Somando...")

        print(f"A soma de {num1} + {num2} é: {resultado}")


    elif menu == 2: 
        num1 = int (input('Digite um número: '))
        num2 = int (input('Digite outro número: '))
        resultado = num1 - num2
        print("Subtraindo...")

        print(f"A soma de {num1} + {num2} é: {resultado}")

    elif menu == 3:
        num1 = int (input('Digite um número: '))
        num2 = int (input('Digite outro número: '))
        resultado = num1 * num2
        print("Multiplicando...")
   
        print(f"A soma de {num1} * {num2} é: {resultado}")

    elif menu == 4:

        num1 = int (input('Digite um número: '))
        num2 = int (input('Digite outro número: '))
        resultado = num1 % num2
        print("Dividindo...")

        print(f"A soma de {num1} % {num2} é: {resultado}")
 
    else: print('Opção inválida. Voltando para o menu inicial...')
    break

