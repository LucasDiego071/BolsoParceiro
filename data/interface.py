import dados_financeiros
import mes
import usuario as user
import streamlit as st
import datetime
import pandas as pd


#===================Inputs Via app===================

st.image("logo.png")

st.title("Bolso :blue[Parceiro]")

st.text("Bem vindo ao Bolso parceiro, Aqui temos a intenção de Organizar suas finanças!")

nome = st.text_input("Insira Seu Nome:", "Joãozinho da Silva")

renda = st.text_input("Insira sua rendas mensais:", "1800.00; 2000.00; 300.00")

gastos = st.text_input("Insira seus gastos fixosm mensais:", "Aluguel = 980.00; Agua = 180.00; Luz = 200.00")

gastos02 = st.text_input("Insira seus gastos extras mensais:", "Cinema = 100.00; Roupas = 300.00")

date = st.date_input("Insira o mês que vai ser organizado:", datetime.date(2024, 2, 1))

# ===================Tratamentos de dados===================
perfil = user.Usuarios(nome)

# ---- Renda:
renda = renda.split(";")

rendas = []

for income in renda:
    income.replace(" ", "")
    income.replace(",", ".")
    income = float(income)
    rendas.append(income)

income = dados_financeiros.Renda(rendas)

# ---- gastos:
gastos = gastos.split(";")

gastos_fixos = []

for gasto in gastos:
    gasto = gasto.split("=")
    gastos_fixos.append(gasto)

for gasto in gastos_fixos:
    gasto[1] = float(gasto[1])


gastos02 = gastos02.split(";")

gastos_extras = []

for gasto in gastos02:
    gasto = gasto.split("=")
    gastos_extras.append(gasto)

for gasto in gastos_extras:
    gasto[1] = float(gasto[1])

gastos_totais = dados_financeiros.Gastos(gastos_fixos, gastos_extras)

# ---- Dados financeiros:

financas = dados_financeiros.Dados_financeiros(income , gastos_totais)

# ---- Mês:
mes = mes.Mes(date, perfil, financas)

# ===================Gerar Tabela===================
st.write(f"{perfil.nome}")
st.write(f"{mes.data}")

lista01 = []
for gastos_fixos in financas.gastos_fixos:
    formatar = {"Descrição" : f"{gastos_fixos[0]}", "Valor": gastos_fixos[1]}
    lista01.append(formatar)

lista02 = []
for gastos_extras in financas.gastos_extras:
    formatar = {"Descrição" : f"{gastos_extras[0]}", "Valor": gastos_extras[1]}
    lista02.append(formatar)

# Convertendo as listas para DataFrames do pandas
df_gastos_fixos = pd.DataFrame(lista01)
df_gastos_extras = pd.DataFrame(lista02)

#calculando os valores:
renda01 = financas.calcular_RendaTotal()
gastos01 = financas.calcular_gastos_fixos()
gastos02 = financas.calcular_gastos_extras()
resto01 = renda01 - gastos01
# Exibindo as tabelas usando st.dataframe()
st.write(f"Seu mês inicia com: R${renda01}")
st.write("Gatos Fixos:")
st.dataframe(df_gastos_fixos)
st.write(f"Após o uso para pagar seus gastos fixos restam: R${renda01 - gastos01}")
st.write(f"Você pode distribuir esse valor entre os gastos extras abaixo.")
st.write("Gastos_Extras:")
st.dataframe(df_gastos_extras)
st.write(f"Caso você gaste o restante com todos os gastos extras, o restante do dinheiro sera: R${resto01 - gastos02}")