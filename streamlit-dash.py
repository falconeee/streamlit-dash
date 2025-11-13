import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Função para gerar dados aleatórios
@st.cache_data
def generate_data(num_points):
    return pd.DataFrame(
        np.random.randn(num_points, 3),
        columns=['A', 'B', 'C']
    )

# Inicializar o Session State
if 'num_points' not in st.session_state:
    st.session_state.num_points = 100

# Configurações do app
st.title("Exemplo Completo de Web App com Streamlit")
st.sidebar.header("Configurações")

# Slider para escolher o número de pontos
num_points = st.sidebar.slider("Escolha o número de pontos:", min_value=10, max_value=500, value=st.session_state.num_points)
st.session_state.num_points = num_points

# Gerar dados com base na escolha do usuário
data = generate_data(st.session_state.num_points)

# Exibir gráficos
st.header("Gráficos")
grafico_tipo = st.selectbox("Escolha o tipo de gráfico:", ["Linha", "Barra", "Área"])
if grafico_tipo == "Linha":
    st.line_chart(data)
elif grafico_tipo == "Barra":
    st.bar_chart(data)
elif grafico_tipo == "Área":
    st.area_chart(data)

# Exibir mapa com dados aleatórios
st.header("Mapa com Dados Aleatórios")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

# Caixas de seleção para mostrar informações adicionais
st.sidebar.header("Opções Adicionais")
show_stats = st.sidebar.checkbox("Mostrar estatísticas descritivas", value=True)
if show_stats:
    st.subheader("Estatísticas Descritivas dos Dados")
    st.write(data.describe())

# Botão para resetar as configurações
if st.sidebar.button("Resetar"):
    st.session_state.num_points = 100
    st.experimental_rerun()