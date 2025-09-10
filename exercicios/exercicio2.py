dicionario = {
    "nome": str,
    "nota": int
}
print(F'nome: {dicionario["nome"]}')
print("nota: dicionario["nota"])

novo_nome = (input ("Digite o nome do aluno/a: "))
dicionario["nome"] = novo_nome
print(f"O aluno {dicionario["nome"]} foi cadastrado")

nova_nota = int (input ("Digite a nota do aluno/a: "))
dicionario["nota"] = nova_nota
print(f"O aluno {dicionario["nome"]} foi avaliado com {dicionario["nota"]}")


print("\n=== MENU ===")
print("1 - Armazenar")
print("2 - Atualizar")
print("3 - Exibir")
print("4 - Voltar para o menu inicial")

# sistema = []
# opçao = 0

# opçao = int(input("Escolha uma opção: "))

# if opçao == 1:
#     Nome = input("Digite o nome do aluno")
#     sistema.append(aluno)
#     print(f"{aluno} adicionado ao sistema")

# elif opçao == 2:
#     if len(sistema) == 0:
#     print(f"Não há alunos cadastrados no sistema")

# elif opçao == 3:
#     aluno = input("Digite o nome do aluno que deseja remover")
#     if aluno in sistema:
#         sistema.remove(aluno)
#     print(f"{aluno} removido do sistema")
# else:
#     print(" Esse aluno não está no sistema")


# # if nota >= 6: 
# #     time.sleep(1.5)  # pausa de 1.5 segundos
# #     print (F'Você está aprovado. Sua nota é {nota}')
# # elif 5 < nota < 6:
# #     time.sleep(1.5)  # pausa de 1.5 segundos
# #     print (F'Você foi pro Conselho de Classe. Sua nota é {nota}')
# # else:
# #     time.sleep(1.5)  # pausa de 1.5 segundos
# #     print (F'Você foi reprovado.')