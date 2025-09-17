+ Bibliotecas de Frontend:
	streamlit
	flet
	kivy
	tkinter
	

1. Criar Ambiente Virtual no Windows:
	 	python -m venv nome_do_ambiente


2. Ativar Ambiente Virtual no Windows:
		nome_do_ambiente//Scripts//activate.ps1

3. Instalar biblioteca Streamlit:
		pip install streamlit

4. Rodar o arquivo python:
		streamlit run nome_do_arquivo.py

===============================

### Importação da Biblioteca

import streamlit as st

st.title("Meu primeiro App")
st.write("Olá Mundo")
===============================

### Primeiro Menu Simples

# st.title("Título Principal")
# st.header("Seções")
# st.subheader("Subseção")

# st.text("Texto simples")
# st.write("Texto formatado ou até **Markdown**")


===============================

### Entrada de Dados

nome = st.text_input ("Digite seu nome: ")
# idade = st.number_input("Digite sua idade: ", min_value=0, max_value=120)

# if st.button("Enviar"):
#     st.success (f"Olá {nome}, você tem {idade} anos!")


===============================

### Lista de Seleção

opcao = st.selectbox("Escolha uma fruta: ", ["Maçã", "Banana", "Sapoti", "Laranja"])
st.write(f"Você escolheu: {opcao}")

===============================

### Upar Imagem 

arquivo = st.file_uploader("Envie uma imagem", type=["png", "jpg", "jpeg"])

if arquivo is not None:
    st.image(arquivo, caption="Imagem enviada", use_container_width=True)