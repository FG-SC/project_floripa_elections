import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página para exibição em modo 'wide'
st.set_page_config(layout="wide")

# Leitura dos dados
df = pd.read_csv('vereadores_info.csv')

# Introdução do aplicativo usando Markdown
st.markdown("""
# Análise de Dados da Campanha Municipal em Florianópolis

Bem-vindo ao aplicativo de análise exploratória dos dados da campanha municipal de Florianópolis! Este dashboard interativo permite que você explore diversas informações sobre os candidatos, partidos políticos e recursos financeiros envolvidos na eleição.

## Funcionalidades

- **Filtro por Partido**: Selecione um partido específico para visualizar dados detalhados sobre seus candidatos.
- **Distribuição Demográfica**: Analise a distribuição de idade, cor, gênero e grau de instrução dos candidatos.
- **Recursos Financeiros**: Explore o total de bens declarados, recursos recebidos e fundos partidários.
- **Despesas Contratadas**: Visualize quais partidos possuem as maiores despesas contratadas.
- **Histórico de Candidaturas**: Identifique os candidatos que mais concorrem e aqueles com maior fundo partidário.

## Como Utilizar

Utilize a barra lateral à esquerda para selecionar o partido de seu interesse ou visualize todos os dados para obter insights abrangentes sobre a campanha. Os gráficos interativos permitirão uma análise detalhada e personalizada conforme suas necessidades.

Vamos explorar juntos os dados e entender melhor a dinâmica da campanha municipal em nossa cidade!
""", unsafe_allow_html=True)

# Título e barra lateral
st.title("Análise Exploratória de Dados por Partido")
partido_options = ['Todos'] + df['Partido'].unique().tolist()
selected_partido = st.sidebar.selectbox("Selecione um Partido", partido_options)

# Filtragem dos dados com base no partido selecionado
if selected_partido != 'Todos':
    filtered_df = df[df['Partido'] == selected_partido]
    st.markdown(f"### Análise do Partido: **{selected_partido}**")
else:
    filtered_df = df
    st.markdown("### Análise de Todos os Partidos")

# Layout de colunas para os gráficos
col1, col2 = st.columns(2)

# 1. Distribuição por Idade (Histograma)
with col1:
    idade_fig = px.histogram(
        filtered_df, 
        x='Idade', 
        nbins=10, 
        color_discrete_sequence=px.colors.sequential.Viridis,
        title='Distribuição por Idade'
    )
    idade_fig.update_layout(
        xaxis_title='Idade',
        yaxis_title='Quantidade',
        bargap=0.1
    )
    st.plotly_chart(idade_fig, use_container_width=True)

# 2. Distribuição por Cor (Gráfico de Pizza)
with col2:
    cor_counts = filtered_df['Cor'].value_counts().reset_index()
    cor_counts.columns = ['Cor', 'Quantidade']
    cor_fig = px.pie(
        cor_counts, 
        names='Cor', 
        values='Quantidade', 
        color='Cor',
        color_discrete_sequence=px.colors.sequential.Viridis,
        title='Distribuição por Cor'
    )
    st.plotly_chart(cor_fig, use_container_width=True)

# 3. Distribuição por Gênero (Gráfico de Pizza)
with col1:
    genero_counts = filtered_df['Gênero'].value_counts().reset_index()
    genero_counts.columns = ['Gênero', 'Quantidade']
    genero_fig = px.pie(
        genero_counts, 
        names='Gênero', 
        values='Quantidade', 
        color='Gênero',
        color_discrete_sequence=px.colors.sequential.Viridis,
        title='Distribuição por Gênero'
    )
    st.plotly_chart(genero_fig, use_container_width=True)

# 4. Distribuição por Grau de Instrução (Histograma)
with col2:
    instrucao_fig = px.histogram(
        filtered_df.sort_values(by = 'Grau de instrução', ascending=False), 
        x='Grau de instrução', 
        color_discrete_sequence=px.colors.sequential.Viridis,
        title='Distribuição por Grau de Instrução'
    )
    instrucao_fig.update_layout(
        xaxis_title='Grau de Instrução',
        yaxis_title='Quantidade',
        bargap=0.1
    )
    st.plotly_chart(instrucao_fig, use_container_width=True)

# Move 'Total de Bens Declarados por Candidato' to a larger section (entire row)
st.markdown("### Total de Bens Declarados por Candidato")
bens_fig = px.bar(
    filtered_df.sort_values(by='Total de Bens Declarados', ascending=False), 
    x='Candidato', 
    y='Total de Bens Declarados', 
    color='Total de Bens Declarados',
    color_discrete_sequence=px.colors.sequential.Viridis,
    title='Total de Bens Declarados por Candidato'
)
bens_fig.update_layout(
    xaxis_title='Candidato',
    yaxis_title='Total de Bens Declarados (R$)',
    showlegend=False
)
st.plotly_chart(bens_fig, use_container_width=True)

# Informações Adicionais Quando 'Todos' é Selecionado
if selected_partido == 'Todos':
    st.markdown("## Insights Adicionais")

    # Partido com mais candidatos
    partido_mais_candidatos = df['Partido'].value_counts().idxmax()
    st.write(f"**Partido com mais candidatos:** {partido_mais_candidatos}")

    # Top 5 Partidos com maiores despesas contratadas - sorting by value
    top5_despesas = df.groupby('Partido')['Total de despesas contratadas (R$)'].sum().sort_values(ascending=False).head(5)

    # Ensure the bars are sorted from largest to smallest
    st.write("**Top 5 Partidos com Maiores Despesas Contratadas:**")
    despesas_fig = px.bar(
        top5_despesas, 
        x=top5_despesas.index, 
        y=top5_despesas.values, 
        color=top5_despesas.values,
        color_discrete_sequence=px.colors.sequential.Viridis,
        title='Despesas Contratadas por Partido'
    )
    despesas_fig.update_layout(
        xaxis_title='Partido',
        yaxis_title='Total de Despesas Contratadas (R$)',
        showlegend=False
    )
    st.plotly_chart(despesas_fig, use_container_width=True)

    # Candidatos que mais concorrem
    top_candidatos_concorrencias = df.sort_values('Vezes em que concorreu', ascending=False).head(5)
    st.write("**Candidatos que mais concorrem:**")
    st.dataframe(top_candidatos_concorrencias[['Candidato', 'Vezes em que concorreu']])

    # Candidatos com maior fundo partidário
    top_candidatos_fundo = df.sort_values('Total de recursos recebidos (R$)', ascending=False).head(5)
    st.write("**Candidatos com Mais Recursos recebidos:**")
    st.dataframe(top_candidatos_fundo[['Candidato', 'Total de recursos recebidos (R$)']])

    # Adicionar mais insights conforme necessário
