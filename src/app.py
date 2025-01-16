#Importando as bibliotecas necessárias:
import pandas as pd
from pathlib import Path
import seaborn as sns
import plotly.express as px
import streamlit as st

#Lendo os dados do df a partir de um caminho relativo
df = pd.read_csv(Path("data/vehicles.csv")) 

#Acrescentando cabeçalho
st.header('Análise de dados de Veiculos')

#Construindo Histograma
fig_hist = px.histogram(df, x="odometer") 
fig_hist.show()

#Construindo gráfico de dispersão
fig_graf = px.scatter(df, x="odometer", y="price") 
fig_graf.show() 

#Implementando botão para o Histograma 
hist_button = st.button('Criar histograma') # criar um botão

if hist_button: # se o botão for clicado escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um histograma
    fig_hist = px.histogram(df, x="odometer")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)

#Implementando botão para o Grafico de dispersão
disp_button = st.button('Criar Gráfico de dispersão') 

if disp_button:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico
    fig_graf = px.scatter(df, x="odometer", y="price") 

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_graf, use_container_width=True)


