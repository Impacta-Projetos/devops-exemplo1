import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Dashboard Clima & Energia - Comparativo", layout="wide")

st.title("Dashboard de Temperatura e Consumo de Energia - São Paulo (Jan-Jun)")

data = {
    'Mês': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho'],
    'Temperatura Média (°C)': [22.3, 22.5, 21.6, 20.2, 17.5, 16.7],
    'Consumo de Energia (MWh)': [1843270, 1785744, 1759933, 1727220, 1686490, 1666694]
}
df = pd.DataFrame(data)

st.subheader("Dados Mensais")
st.dataframe(df)


st.subheader("Temperatura Média Mensal")
fig_temp = px.line(
    df,
    x='Mês',
    y='Temperatura Média (°C)',
    markers=True,
    text='Temperatura Média (°C)',
    labels={'Temperatura Média (°C)': 'Temperatura (°C)', 'Mês': 'Mês'}
)
fig_temp.update_traces(
    line=dict(color='#FF7F0E', width=3),
    textposition='top center'
)
fig_temp.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='rgba(240,240,240,1)',
    font=dict(size=14, color='black'),
    xaxis=dict(title='', tickfont=dict(color='black', size=14)),
    yaxis=dict(title=dict(text='Temperatura (°C)', font=dict(size=14, color='black')), tickfont=dict(color='black', size=14))
)
st.plotly_chart(fig_temp, use_container_width=True)


st.subheader("Consumo de Energia Mensal")
fig_cons = px.line(
    df,
    x='Mês',
    y='Consumo de Energia (MWh)',
    markers=True,
    text='Consumo de Energia (MWh)',
    labels={'Consumo de Energia (MWh)': 'Consumo (MWh)', 'Mês': 'Mês'}
)
fig_cons.update_traces(
    line=dict(color='#1F77B4', width=3),
    textposition='top center'
)
fig_cons.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='rgba(240,240,240,1)',
    font=dict(size=14, color='black'),
    xaxis=dict(title='', tickfont=dict(color='black', size=14)),
    yaxis=dict(title=dict(text='Consumo (MWh)', font=dict(size=14, color='black')), tickfont=dict(color='black', size=14))
)
st.plotly_chart(fig_cons, use_container_width=True)


st.subheader("Comparativo: Temperatura vs Consumo de Energia")
fig_comp = go.Figure()


fig_comp.add_trace(go.Scatter(
    x=df['Mês'],
    y=df['Temperatura Média (°C)'],
    name='Temperatura (°C)',
    mode='lines+markers',
    line=dict(color='#FF7F0E', width=3),
    yaxis='y1'
))


fig_comp.add_trace(go.Scatter(
    x=df['Mês'],
    y=df['Consumo de Energia (MWh)'],
    name='Consumo (MWh)',
    mode='lines+markers',
    line=dict(color='#1F77B4', width=3),
    yaxis='y2'
))


fig_comp.update_layout(
    xaxis=dict(title='', tickfont=dict(color='black', size=14)),
    yaxis=dict(title=dict(text="Temperatura (°C)", font=dict(color='#FF7F0E', size=14)),
               tickfont=dict(color='#FF7F0E', size=14)),
    yaxis2=dict(title=dict(text="Consumo de Energia (MWh)", font=dict(color='#1F77B4', size=14)),
                tickfont=dict(color='#1F77B4', size=14),
                overlaying="y",
                side="right"),
    legend=dict(orientation="h", x=0.5, y=-0.2, xanchor="center", font=dict(color='black', size=14)),
    plot_bgcolor='white',
    paper_bgcolor='rgba(240,240,240,1)',
    font=dict(size=14, color='black')
)
st.plotly_chart(fig_comp, use_container_width=True)


st.subheader("Métricas")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Média de Temperatura (°C)",
        value=f"{df['Temperatura Média (°C)'].mean():.1f}"
    )

with col2:
    st.metric(
        label="Média de Consumo (MWh)",
        value=f"{df['Consumo de Energia (MWh)'].mean():,.0f}"
    )

with col3:
    inicio = df['Consumo de Energia (MWh)'].iloc[0]
    fim = df['Consumo de Energia (MWh)'].iloc[-1]
    variacao = ((fim - inicio) / inicio) * 100
    st.metric(
        label="Variação do Consumo (%)",
        value=f"{variacao:.2f}%"
    )
