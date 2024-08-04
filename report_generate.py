import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data
def load_data():
    data = pd.read_csv("data/users.csv")
    return data

data = load_data()

st.title('Relatorio de Vendas')

st.subheader('Dados Brutos')
st.write(data)

dados_produto = data.groupby('Nome do Produto').agg({
    'Quantidade' : 'sum',
    'Lucro' : ['sum', 'mean', 'std']
})

data_graphs = data.groupby('Nome do Produto').sum()

st.subheader("Valores Por Produto")
figura_quantidade = px.bar(data_graphs, 
                           x = data_graphs.index,
                           y = 'Quantidade',
                           title = "Quantidade x Produto")

st.plotly_chart(figura_quantidade)

figura_receita = px.bar(data_graphs,
                        x = data_graphs.index,
                        y = 'Lucro',
                        title ="Receita x Produto" )

st.plotly_chart(figura_receita)

# Exibindo o total de receita e quantidade vendida
st.subheader('Resumo Geral')
st.write('Total de Receita : R$', data['Lucro'].sum())
st.write('Total de Quantidade:', data['Quantidade'].sum())


# Exibindo estatisticas adicionais
st.subheader('Estatística Adicionais')
st.write('Média de Receita por Produto:')
st.write(dados_produto['Lucro']['mean'])
st.write('Desvio Padrão de Receita por Produto:')
st.write(dados_produto['Lucro']['std'])




# Recomendações com base nos dados
st.subheader('Recomendações')
media_receita = dados_produto['Lucro']['mean'].mean()
desvio_padrao_medio = dados_produto['Lucro']['std'].mean()


st.write('Média Receita Geral:', media_receita)
st.write('Desvio Parão Médio:', desvio_padrao_medio)

if media_receita < 500 : 
    st.write('Concentra-se nos produtos com receita média mais alta.')
elif desvio_padrao_medio > 100 : 
    st.write('Aborde a varabilidade da receita de alguns produtos.')
else :
    st.write('Manter a estratégia.')