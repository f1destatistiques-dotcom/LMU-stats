import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(layout="wide") # Permet un affichage en plein écran


# PERMET LA LECTURE DU FICHIER CSV STOCKÉ DANS LES DÉPÔTS DE GITHUB (MES PROPRES DÉPOTS)
import pandas as pd

url_lap_by_circuit = "https://raw.githubusercontent.com/f1destatistiques-dotcom/LMU-stats/refs/heads/main/laps_by_circuit.csv"
df_lap_by_circuit = pd.read_csv(url_lap_by_circuit, encoding="latin-1")

# df_sorted = df_lap_by_circuit.sort_values("Tours", ascending=True)
# st.bar_chart(df_sorted.set_index("Circuit")["Tours"])


# GRAPH DU NOMBRE DE TOURS PAR CIRCUITS______________________________________________

df_sorted = df_lap_by_circuit.sort_values("Value", ascending=False)

fig = px.bar(
    df_sorted,
    x="Track",
    y="Value",
    text="Value",
    title="Nombre de tours par circuit (croissant)",
)

fig.update_layout(height=800)
#fig.update_traces(marker_pattern_shape="/")
fig.update_traces(width=0.4)

st.plotly_chart(fig, use_container_width=True, config={"staticPlot": True})


# GRAPH DE LA POSITION D'ARRIVÉE DES 20 DERNIÈRES COURSES______________________________________________

url_last_20_races = "https://raw.githubusercontent.com/f1destatistiques-dotcom/LMU-stats/refs/heads/main/last_20.csv"
df_last_20_races = pd.read_csv(url_last_20_races, encoding="latin-1")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x = df_last_20_races["Course"],
    y = df_last_20_races["Position"],
    mode="lines+markers",
    line=dict(color="#83A6D1", width=1),
    marker=dict(size=5, color="#83A6D1"),
    fill="tozeroy",              # Remplissage sous la courbe
    line_shape="spline",         # Courbe arrondie
    name="Position"
))

fig.add_hline(
    y=5,
    line_width=1,
    line_dash="dash",
    line_color="purple",
    annotation_text="Top 5",
    annotation_position="right"
)

fig.add_hline(
    y=10,
    line_width=1,
    line_dash="dash",
    line_color="orange",
    annotation_text="Top 10",
    annotation_position="right"
)

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


# ---- Rajout d'une courbe de tendance -------------------
# x = numéro de course
x = df_last_20_races["Course"]
# y = position
y = df_last_20_races["Position"]
# Régression linéaire : y = a*x + b
a, b = np.polyfit(x, y, 1)
# Valeurs de la tendance
df_last_20_races["Trend"] = a * x + b

fig.add_trace(go.Scatter(
    x=df_last_20_races["Course"],
    y=df_last_20_races["Trend"],
    mode="lines",
    line=dict(color="black", width=1, dash="dot"),
    name="Tendance"
))







st.plotly_chart(fig, config={"staticPlot": True})
