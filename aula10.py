============
MODULARIZAÇÃO
============

----------------- main.py

# Modularização == atribuir, ou anexar valores/métodos/funções de outro arquivo no meu arquivo principal

import functions                                              		# modularização/importação total  
import funcitions as fn                                    		# modularização/importação total com alias (apelido)
from functions import somar                        		# modularização/importação específica
from functions import somar, subtrair	     		# modularização/importação específica múltipla
from functions import somar as sm            		# modularização/importação específica com alias


from functions import *                                		# modularização/importação coringa ou global == má prática

while True:
    print("\n=== Calculadora Simples ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

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


----------------- functions.py

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

================
BIBLIOTECA
================

# import math

# print(math.sqrt(16))      # raiz quadrada 
# print(math.factorial(5))  # fatorial 5! == 
# print(math.pi)            # valor de PI

# from random import randint, choice
# print(randint(1, 10))  # número inteiro entre 1 e 10
# print(choice(["maçã", "banana", "uva"]))  # escolhe um elemento da lista

# import datetime

# hoje = datetime.date.today()
# print("Hoje é:", hoje)

# agora = datetime.datetime.now()
# print("Data e hora atuais:", agora)

import time

print("Início do programa...")
time.sleep(0.5)  # pausa por .5 segundo
print("10...")
time.sleep(1)  # pausa por 1 segundo
print("9...")
time.sleep(1)  # pausa por 1 segundo
print("8...")
time.sleep(1)  # pausa por 1 segundo
print("7...")
time.sleep(1)  # pausa por 1 segundo
print("6...")
time.sleep(1)  # pausa por 1 segundo
print("5...")
time.sleep(1)  # pausa por 1 segundo
print("4...")
time.sleep(1)  # pausa por 1 segundo
print("3...")
time.sleep(1)  # pausa por 1 segundo
print("2...")
time.sleep(1)  # pausa por 1 segundo
print("1...")
time.sleep(1)  # pausa por 1 segundo
print("Feliz Ano Novo")



=============
*ARGS E **KWARGS
=============

# *args = argumentos posicionais (quantidade variável, recebidos como tupla).

# **kwargs = argumentos nomeados (quantidade variável, recebidos como dicionário)

# def soma(*args):
#     return sum(args)

# print(soma(1, 2, 3))       # 6
# print(soma(10, 20, 30, 40)) # 100


# def juntar_palavras(*args):
#     return " ".join(args)

# print(juntar_palavras("Olá", "mundo"))         # "Olá mundo"
# print(juntar_palavras("Python", "é", "legal")) # "Python é legal"


# def maior(*args):
#     return max(args)

# print(maior(3, 8, 2, 10)) # 10


# def lista_compras(*args):
#     for item in args:
#         print("•", item)

# lista_compras("Arroz", "Feijão", "Macarrão")


# def media(*args):
#     return sum(args) / len(args)

# print(media(7, 8, 9))  # 8.0


# # ===============================================


# def mostrar_pessoa(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f"{chave}: {valor}")

# mostrar_pessoa(nome="Ana", idade=25, cidade="Salvador")


# def configurar_jogo(**kwargs):
#     print("Configurações do jogo:")
#     for chave, valor in kwargs.items():
#         print(f"{chave} = {valor}")

# configurar_jogo(dificuldade="Médio", som=True, vidas=3)


# def produto(**kwargs):
#     return kwargs

# print(produto(nome="Notebook", preco=3500, estoque=12))


# def mensagem(**kwargs):
#     print(f"Olá {kwargs.get('nome', 'Usuário')}!")
#     print(f"Bem-vindo(a) a {kwargs.get('plataforma', 'nossa aplicação')}.")

# mensagem(nome="Carlos", plataforma="PythonApp")


# def registrar_notas(**kwargs):
#     for materia, nota in kwargs.items():
#         print(f"{materia}: {nota}")

# registrar_notas(Mat="8.5", Português="7.0", Inglês="9.0")


# # ===============================================


def pedido (*args, **kwargs):
    itens = list(args)
    usuarios = kwargs

    print (f'Pedidos Confirmados: {itens}')
    print (f'Usuários cadastrados: {usuarios}')

#      |            ARGS                 |                KWARGS                     |
pedido ("Pizza", "Refrigerante", "Cookie", user="Daniel77", endereco="Rua das Flores")










=============================================
						Conceito:
============================================

=====================  Modularização  =====================

É o processo de organizar seu código em módulos, ou seja, em arquivos separados (como functions.py), cada um com funções, classes ou variáveis específicas.

Facilita a organização, manutenção e reaproveitamento do código.

Exemplo: você cria um módulo functions.py com várias funções para usar em vários programas.

=====================  Importação   =====================

É a ação de trazer para seu programa o conteúdo de um módulo (arquivo) que você modularizou.

Ou seja, quando você escreve import functions, está importando o módulo que foi criado.

Importação é a forma como você usa a modularização.