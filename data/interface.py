'''import data.dados_financeiros as data_money
import data.mes as month'''
import data.usuario as user
import streamlit as st



st.image("logo.png")
st.title("Bolso :blue[Parceiro]")

st.text("Bem vindo ao Bolso parceiro, Aqui temos a intenção de Organizar suas finanças!")

nome = st.text_input("Insira Seu Nome:", "João Santos da Silva")

perfil = user.Usuarios(nome)

