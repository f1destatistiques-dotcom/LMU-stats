import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(layout="wide") # Permet un affichage en plein écran


# PERMET LA LECTURE DU FICHIER CSV STOCKÉ DANS LES DÉPÔTS DE GITHUB (MES PROPRES DÉPOTS)
import pandas as pd

url_lap_by_circuit = "https://raw.githubusercontent.com/f1destatistiques-dotcom/LMU-stats/refs/heads/main/laps_by_circuit.csv"
df_lap_by_circuit = pd.read_csv(url_lap_by_circuit)

# df_sorted = df_lap_by_circuit.sort_values("Tours", ascending=True)
# st.bar_chart(df_sorted.set_index("Circuit")["Tours"])


# GRAPH DU NOMBRE DE TOURS PAR CIRCUITS______________________________________________

df_sorted = df_lap_by_circuit.sort_values("Tours", ascending=False)

fig = px.bar(
    df_sorted,
    x="Circuit",
    y="Tours",
    text="Tours",
    title="Nombre de tours par circuit (croissant)",
)

fig.update_layout(height=800)
#fig.update_traces(marker_pattern_shape="/")
fig.update_traces(width=0.4)

st.plotly_chart(fig, use_container_width=True)


# GRAPH DE LA POSITION D'ARRIVÉE DES 20 DERNIÈRES COURSES______________________________________________

url_last_20_races = "https://raw.githubusercontent.com/f1destatistiques-dotcom/LMU-stats/refs/heads/main/last_20.csv"
df_last_20_races = pd.read_csv(url_last_20_races)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x = df_last_20_races["Course"],
    y = df_last_20_races["Position"],
    mode="lines+markers",
    line=dict(color="#5784BA", width=3),
    marker=dict(size=10, color="#4B79B1"),
    fill="tozeroy",              # Remplissage sous la courbe
    line_shape="spline",         # Courbe arrondie
    name="Position"
))

# # --- Labels séparés (toujours visibles) ---
# fig.add_trace(go.Scatter(
#     x=df_last_20_races["Course"],
#     y=df_last_20_races["Position"],
#     mode="text",
#     text=df_last_20_races["Position"],
#     textposition="top center",
#     textfont=dict(color="black", size=14),
#     showlegend=False
# ))

st.plotly_chart(fig, config = {'scrollZoom': False})
