import streamlit as st

st.set_page_config(layout="wide") # Permet un affichage en plein écran


# PERMET LA LECTURE DU FICHIER CSV STOCKÉ DANS LES DÉPÔTS DE GITHUB (MES PROPRES DÉPOTS)
import pandas as pd

url_lap_by_circuit = "https://raw.githubusercontent.com/f1destatistiques-dotcom/LMU-stats/refs/heads/main/laps_by_circuit.csv"
df_lap_by_circuit = pd.read_csv(url_lap_by_circuit)

# df_sorted = df_lap_by_circuit.sort_values("Tours", ascending=True)
# st.bar_chart(df_sorted.set_index("Circuit")["Tours"])


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
