tarefas = {}
dias = []
tarefas[dias] = []

# Dentro do dicionário dias e tarefas, respectivamente:
dia = []
plano = []

while True:
    menu = int(input('''
            --- PLANNER ---
                1. Editar tarefas
                2. Visualizar lista semanal
                3. Visualizar lista por dia
                4. Sair

           '''))

    if menu == 3:
        while True:
            menu = int(input('''
        1. Segunda                                               
        2. Terça                                               
        3. Quarta                                               
        4. Quinta                                             
        5. Sexta                                    
        6. Sabado            
            '''))

    if menu == 1:
          for i in Segunda(len(dias)):
                print(f"{i}-{dias[i]} (Tarefas: {tarefas[i]})")


    opcao = input("Escolha uma opçao")

    if opcao == "1":
        dias = input("Escolha o dia da semana")
        dia.append(dias)
        print("Adicionando anotação...")
        tarefas = input("Qual seu plano para hoje?")
        if dias not in tarefas:
        tarefas[dias].append(tarefas)
        print("Sua tarefa foi inserida!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Você não tem tarefas para hoje")
        else:
            for i in dia(len(dias)):
                print(f"{i}-{dias[i]} (Tarefas: {tarefas[i]})")

    elif opcao == "3":
        if len(tarefas) == 0:
            print("Você não tem tarefas para hoje")
        else:
            for i in dia(len(dias)):
                print(f"{i}-{dias[i]} (Tarefas: {tarefas[i]})")


    elif opcao == "4":
        print("Voltando para a tela inicial...")
        break
    

