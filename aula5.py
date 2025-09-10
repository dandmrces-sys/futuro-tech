'''
    1. Tabuada 
'''
# numero = int(input("Digite um número para ver a tabuada: "))

# print(f"\nTabuada do {numero}:")
# for i in range(1, 11):
#     print(f"{numero} x {i} = {numero * i}")

'''

#codigo_luan.py
numero = int(input("Digite um valor: "))

for i in range(-5,11,3):
    resultado = numero*i
    print(f"{numero}x{i}={resultado}")

#codigo_pedro.py
# numero = int(input("Digite o número para multiplicação: "))
# cont = 1 

# while cont < 11:
#     print(f'{cont} * {numero} = {cont*numero}')
#     cont += 1


#codigo_marlon.py
# lista = [1,2,3,4,5,6,7,8,9,10]
# tabuada = int(input("Você quer a tabuada de qual número?"))

# resultado = tabuada * lista

# for i in lista:
#     print(resultado)




    2. Contagem 1 a 10
'''
# print("Contando de 1 a 10:")
# for i in range(1, 11):
#     print(i)

'''
    3. Soma e média
'''
numeros = [5,100,10,20,30]

# for i in numeros:
#     media = sum(numeros) / len(numeros)

# print (f'A média da lista {numeros} é {media}')

'''
    4. Pedir senha ao usuário e parar dps de 3 tentativas
'''
# senha_correta = "python123"

# tentativas = 0
# limite = 3

# while tentativas < limite:
#     senha = input("Digite a senha: ")
#     if senha == senha_correta:
#         print("Acesso liberado! ✅")
#         break
#     else:
#         tentativas += 1
#         print(f"Senha incorreta! Tentativas restantes: {limite - tentativas}")

# if tentativas == limite:
#     print("Acesso bloqueado. Número máximo de tentativas atingido. ❌")
'''
    5. Carrinho de Compras Simples
'''
# carrinho = []
# opcao = 0

# while opcao != 4:
#     print("\n=== MENU CARRINHO DE COMPRAS ===")
#     print("1 - Adicionar item")
#     print("2 - Remover item")
#     print("3 - Listar itens do carrinho")
#     print("4 - Finalizar compra")

#     opcao = int(input("Escolha uma opção: "))

#     if opcao == 1:
#         item = input("Digite o nome do produto que deseja adicionar: ")
#         carrinho.append(item)
#         print(f"{item} adicionado ao carrinho.")

#     elif opcao == 2:
#         if len(carrinho) == 0:
#             print("O carrinho está vazio!")
#         else:
#             item = input("Digite o nome do produto que deseja remover: ")
#             if item in carrinho:
#                 carrinho.remove(item)
#                 print(f"{item} removido do carrinho.")
#             else:
#                 print("Esse item não está no carrinho.")

#     elif opcao == 3:
#         if len(carrinho) == 0:
#             print("Carrinho vazio.")
#         else:
#             print("Itens no carrinho:")
#             for produto in carrinho:
#                 print("-", produto)

#     elif opcao == 4:
#         print("Compra finalizada! Obrigado por comprar conosco.")
#         print("Itens comprados:", carrinho)

#     else:
#         print("Opção inválida, tente novamente.")


'''
FOR + RANGE()
'''

# for i in range(1, 11):
#     print(i)

# for i in range(0, 21, 2):
#     print(i)

# soma = 0
# for i in range(1, 101):
#     soma += i
# print("Soma de 1 a 100 =", soma)


'''
    Dicionários:
'''

# dicionario = {}

'''
    Dicionários:

'''

lista = []
tupla = ()
dicionario = {}

# C R U D 

# CREATE = CRIAR
dicionario = {
    "nome": str,
    "idade": int,
    "nota": int
}

# READ = LER
# print(F'Nome: {dicionario["nome"]}')
# print("Idade:", dicionario["idade"])
# print("Nota:", dicionario["nota"])

# print(dicionario.keys())
# print(dicionario.values())
# print(dicionario.items())

# UPDATE = ATUALIZAR
novo_nome = (input ("Digite o nome do aluno/a: "))
dicionario["nome"] = novo_nome
print(f"O aluno {dicionario["nome"]} foi cadastrado")

nova_nota = int (input ("Digite a nota do aluno/a: "))
dicionario["nota"] = nova_nota
print(f"O aluno {dicionario["nome"]} foi avaliado com {dicionario["nota"]}")

nova_idade = int (input ("Digite a idade do aluno/a: "))
dicionario["idade"] = nova_idade
print(f"Idade do aluno/a {dicionario["nome"]} atualizada para {dicionario["idade"]}")
print (dicionario)


# for i, j in aluno.items():
#     print(i, ":", j)

# nova_cidade = input('Digite a cidade do aluno: ')
# dicionario["cidade"] = nova_cidade
# print(dicionario)


# DELETE = DELETAR
del dicionario["idade"]
print(dicionario)



