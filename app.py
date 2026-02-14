import pandas as pd
import plotly.express as px
import streamlit as st

# Dados fictícios para os 13 municípios
dados_lista = [
    {"Município": "São Luís", "Empregados": 350000, "Desempregados": 50000, "Renda < 1 SM": 120000, "lat": -2.53, "lon": -44.30},
    {"Município": "Paço do Lumiar", "Empregados": 80000, "Desempregados": 15000, "Renda < 1 SM": 40000, "lat": -2.53, "lon": -44.10},
    {"Município": "Raposa", "Empregados": 30000, "Desempregados": 5000, "Renda < 1 SM": 15000, "lat": -2.42, "lon": -44.10},
    {"Município": "São José de Ribamar", "Empregados": 120000, "Desempregados": 20000, "Renda < 1 SM": 60000, "lat": -2.56, "lon": -44.05},
    {"Município": "Alcântara", "Empregados": 25000, "Desempregados": 4000, "Renda < 1 SM": 12000, "lat": -2.41, "lon": -44.41},
    {"Município": "Bacabeira", "Empregados": 20000, "Desempregados": 3000, "Renda < 1 SM": 10000, "lat": -2.55, "lon": -44.32},
    {"Município": "Cachoeira Grande", "Empregados": 15000, "Desempregados": 2000, "Renda < 1 SM": 8000, "lat": -2.93, "lon": -44.05},
    {"Município": "Icatu", "Empregados": 18000, "Desempregados": 2500, "Renda < 1 SM": 9000, "lat": -2.77, "lon": -44.05},
    {"Município": "Morros", "Empregados": 22000, "Desempregados": 3500, "Renda < 1 SM": 11000, "lat": -2.85, "lon": -44.04},
    {"Município": "Presidente Juscelino", "Empregados": 12000, "Desempregados": 1800, "Renda < 1 SM": 6000, "lat": -2.92, "lon": -44.07},
    {"Município": "Rosário", "Empregados": 40000, "Desempregados": 6000, "Renda < 1 SM": 20000, "lat": -2.93, "lon": -44.25},
    {"Município": "Santa Rita", "Empregados": 35000, "Desempregados": 5000, "Renda < 1 SM": 17000, "lat": -3.13, "lon": -44.32},
    {"Município": "Axixá", "Empregados": 10000, "Desempregados": 1500, "Renda < 1 SM": 5000, "lat": -2.83, "lon": -44.05}
]

df = pd.DataFrame(dados_lista)

# Gráfico comparativo
df_long = df.melt(id_vars="Município", 
                  value_vars=["Empregados", "Desempregados"], 
                  var_name="Categoria", 
                  value_name="Valor")

cores = {"Empregados": "green", "Desempregados": "red"}

st.title("Dashboard - Comparação dos Municípios da Região Metropolitana de São Luís (dados fictícios)")

fig_bar = px.bar(df_long, 
                 x="Município", 
                 y="Valor", 
                 color="Categoria", 
                 title="Empregados vs Desempregados",
                 color_discrete_map=cores,
                 barmode="group")
st.plotly_chart(fig_bar)

# Mapa interativo
fig_map = px.scatter_geo(df, 
                         lat="lat", lon="lon",
                         text="Município",
                         size="Empregados",
                         color="Desempregados",
                         title="Mapa da Região Metropolitana de São Luís - Empregados e Desempregados",
                         projection="mercator")

# Nome dos municípios em vermelho
fig_map.update_traces(textfont=dict(color="red"))

st.plotly_chart(fig_map)

# Tabela
st.dataframe(df)