import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Carregar o arquivo CSV
df = pd.read_csv("data/tratado.csv")

# Converter a coluna 'data' para o formato datetime
df["data"] = pd.to_datetime(df["data"])
df["mes"] = df["data"].dt.to_period("M")  # Adicionar coluna de mês

# Título do app
st.title("Dashboard de Análise de Dados Financeiros")

# Filtros interativos
preco_min = st.slider("Filtrar por preço mínimo", min_value=0, max_value=500, value=50)
produto_selecionado = st.multiselect(
    "Filtrar por produto",
    options=df["produto"].unique(),
    default=df["produto"].unique(),
)

# Aplicar filtros
df_filtrado = df[(df["preco"] >= preco_min) & (df["produto"].isin(produto_selecionado))]

# Mostrar tabela filtrada
st.subheader("Dados filtrados")
st.write(df_filtrado)

# Evolução da quantidade de vendas por produto
st.subheader("Evolução da Quantidade de Vendas por Produto")
vendas_por_produto = (
    df_filtrado.groupby(["mes", "produto"])["quantidade"].sum().unstack()
)

# Opção de visualização: Linha ou Barras
tipo_grafico = st.radio("Escolha o tipo de gráfico", ("Linha", "Barras"))

if tipo_grafico == "Linha":
    st.line_chart(vendas_por_produto)
else:
    stacked = st.radio("Empilhado", ("Sim", "Não"))
    if stacked == "Sim":
        vendas_por_produto.plot(kind="bar", stacked=True, figsize=(10, 6))
    else:
        vendas_por_produto.plot(kind="bar", figsize=(10, 6))
    st.pyplot(plt)

# Evolução do lucro por mês
st.subheader("Evolução do Lucro por Mês")
df_filtrado["lucro"] = df_filtrado["receita"] - df_filtrado["custos"]
lucro_por_mes = (
    df_filtrado.groupby(["mes", "produto"])["lucro"].sum().unstack(fill_value=0)
)

# Filtro para visualizar todos os produtos juntos ou por produto
visualizar_por_produto = st.checkbox("Visualizar lucro por produto")

if visualizar_por_produto:
    st.line_chart(lucro_por_mes)
else:
    lucro_total_por_mes = df_filtrado.groupby("mes")["lucro"].sum()
    st.line_chart(lucro_total_por_mes)
