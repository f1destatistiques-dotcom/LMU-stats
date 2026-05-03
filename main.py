import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

#st.set_page_config(layout="wide") # Permet un affichage en plein écran

st.sidebar.success('Homer')

#Pour lancer l'environnement virtual
# cd virtenv
# streamlit run main.py

st.title("LMU RAMCO Stats 🏆")

# PERMET LA LECTURE DU FICHIER CSV STOCKÉ DANS LES DÉPÔTS DE GITHUB (MES PROPRES DÉPOTS)
import pandas as pd
url_general_data = "https://raw.githubusercontent.com/f1destatistiques-dotcom/LMU-stats/refs/heads/main/general_data.csv"
df_general_data = pd.read_csv(url_general_data, encoding="latin-1")

url_lap_by_circuit = "https://raw.githubusercontent.com/f1destatistiques-dotcom/LMU-stats/refs/heads/main/laps_by_circuit.csv"
df_lap_by_circuit = pd.read_csv(url_lap_by_circuit, encoding="latin-1")

# AFFICHER TOUT LE TABLEAU CSV
#st.dataframe(df_general_data)


# -------------------------------- N'affiche que les data Tours du fichier DATA général + filtrage possible_____________________
ordre = ["Toutes", "GT3", "GTE", "LMP2", "LMP2_ELMS", "LMP3", "Hypercar"]
# categories = df_general_data["Category"].dropna().unique()
# cat_choice = st.selectbox("Choisir une catégorie :", categories)

# On filtre pour ne garder que les catégories présentes dans le CSV
categories = [cat for cat in ordre if cat in df_general_data["Category"].unique()]
cat_choice = st.selectbox("Choisir une catégorie :", categories)


filtered = df_general_data[df_general_data["Category"] == cat_choice]

# st.dataframe(filtered) # Affichage sous forme de tableau

# CHOIX DES ICONES POUR LES TUILES
icons = {
    "Nombre de courses en multi": "🏁",
    "Nombre de tours": "🕓",
    "Nombre de victoires / Ratio": "🏆",
    "Nombre de podiums / Ratio": "🥉",
    "Nombre de TOP 5 / Ratio": "5️⃣",
    "Nombre de TOP10 / Ratio": "🔟",
    "Nombre de poles": "🎯",
    "Position moyenne en course": "🚥",
    "Position moyenne en Qualif.": "🛞",
    "Nombre de DNF" : "🏴"
}

#for _, row in filtered.iterrows():
    #st.metric(label=row["Data"], value=row["Value"]) # Affichage dans une tuile simple

cols = st.columns(3)
filtered = filtered.reset_index(drop=True)  # <<< Permet de forcer d'afficher la première tuile à gauche

for i, row in filtered.iterrows():
    label = row["Data"]
    value = row["Value"]
    icon = icons.get(label, "❓")

    col = cols[i % 3]  # 0,1,2 puis 0,1,2...
    #col = st.columns(cols)

    with col:
        st.markdown(f"""
            <div style="
                background-color:#EEE6D8;
                padding:10px;
                border-radius:12px;
                text-align:center;
                color:black;
                width:100%;
                margin-bottom:20px;">
                <div style="font-size:40px; margin-bottom:10px;">{icon}</div>
                <div style="font-size:14px; opacity:0.7;">{label}</div>
                <div style="font-size:32px; font-weight:700; margin-top:1px;">{value}</div>
            </div>
        """, unsafe_allow_html=True)







# GRAPH DE LA POSITION D'ARRIVÉE DES 20 DERNIÈRES COURSES______________________________________________

st.subheader("Historique des 20 dernières courses (toute catégorie)")

url_last_20_races = "https://raw.githubusercontent.com/f1destatistiques-dotcom/LMU-stats/refs/heads/main/last_20.csv"
df_last_20_races = pd.read_csv(url_last_20_races)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x = df_last_20_races["Course"],
    y = df_last_20_races["Position"],
    mode="lines+markers",
    line=dict(color="#83A6D1", width=1),
    marker=dict(size=5, color="#83A6D1"),
    fill="tozeroy",              # Remplissage sous la courbe
    #line_shape="spline",         # Courbe arrondie$
    line_shape="hvh",
    name="Position"
))

fig.add_hline(
    y=5,
    line_width=1,
    line_dash="dash",
    line_color="blue",
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


st.plotly_chart(fig, config={"staticPlot": True})



# GRAPH  de la somme des 20 dernières courses

st.subheader("Somme de position des 20 dernières courses")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x = df_last_20_races["Course"],
    y = df_last_20_races["Somme_20_courses"],
    mode="lines+markers",
    line=dict(color="#83A6D1", width=1),
    marker=dict(size=5, color="#83A6D1"),
    #fill="tozeroy",              # Remplissage sous la courbe
    line_shape="spline",         # Courbe arrondie$
    #line_shape="hvh",              # Course en escalier
    name="Somme_20_courses"
))

fig.add_hline(
    y=200,
    line_width=1,
    line_dash="dash",
    line_color="blue",
    annotation_text="TOP10",
    annotation_position="right"
)

st.plotly_chart(fig)


















# CHOIX DES ICONES POUR LES TUILES
# icons = {
#     "Nombre de courses en multi": "🏁",
#     "Nombre de tours": "🕓",
#     "Nombre de victoires": "🏆",
#     "Nombre de podiums / Ratio": "🥉",
#     "Nombre de TOP 5 / Ratio": "5️⃣",
#     "Nombre de TOP 10 / Ratio": "🔟",
#     "Nombre de poles": "🎯",
#     "Position moyenne en course": "🚥",
#     "Position moyenne en Qualif.": "🛞",
# }

# # Nombre de tuiles par ligne
# tiles_per_row = 3

# # TILES POPULATING
# for i in range(0, len(df_general_data), tiles_per_row):
#     cols = st.columns(tiles_per_row)

#     for j in range(tiles_per_row):
#         if i + j < len(df_general_data):
#             row = df_general_data.iloc[i + j]
#             label = row["Data"]
#             value = row["Value"]
#             icon = icons.get(label, "❓")

#             with cols[j]:
#                 st.markdown(f"""
#                     <div style="
#                         background-color:#EEE6D8;
#                         padding:10px;
#                         border-radius:12px;
#                         text-align:center;
#                         color:black;
#                         width:100%;
#                         margin-bottom:20px;">
#                         <div style="font-size:40px; margin-bottom:10px;">{icon}</div>
#                         <div style="font-size:14px; opacity:0.7;">{label}</div>
#                         <div style="font-size:32px; font-weight:700; margin-top:1px;">{value}</div>
#                     </div>
#                 """, unsafe_allow_html=True)


# Choisir les colonnes du CSV à afficher
#colonnes = ["Circuit", "Voiture", "Record"]
#df_filtre = df[colonnes]
#st.dataframe(df_filtre)

# FILTRE SUR UNE VOITURE
# Voiture = st.selectbox("Choisir une voiture :", df["Voiture"].unique())
# df_filtre = df[df["Voiture"] == Voiture]
# st.dataframe(df_filtre)

# FILTRE SUR UNE VOITURE AVEC LA POSSIBILITÉ DE L'IGNORER
# Voiture = st.selectbox("Voiture :", ["Toutes"] + list(df["Voiture"].unique()))
# df_filtre = df[df["Voiture"] == Voiture]

# if Voiture != "Toutes":
#     df_filtre = df[df["Voiture"] == Voiture]
#     st.dataframe(df_filtre)

# AFFICHER UNE VALEUR DANS UNE TUILE
#record_value = df_filtre["Record"].iloc[0]
#st.metric(label="Record", value=record_value)

# AFFICHER UNE VALEUR DANS UNE TUILE PERSONNALISÉE
# if not df_filtre.empty:
#     record_value = df_filtre["Record"].iloc[0]

#     st.markdown(f"""
#         <div style="
#             background-color:#262730;
#             padding:20px;
#             border-radius:12px;
#             text-align:center;
#             color:white;">
#             <div style="font-size:14px; opacity:0.7;">Record</div>
#             <div style="font-size:40px; font-weight:700;">{record_value}</div>
#             <div style="font-size:12px; opacity:0.5;">Valeur filtrée</div>
#         </div>
#     """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

#car_value = df_filtre["Voiture"].iloc[0]

# with col1:
#     st.markdown(f"""
#         <div style="
#             background-color:#D6D6D6;
#             padding:15px;
#             border-radius:12px;
#             text-align:center;
#             color:black ;">
#             <img src="https://gpticketstore.vshcdn.net/uploads/images/15641/file.jpg" style="width:100%; border-radius:8px;">
#             <div style="font-size:14px; opacity:0.7; margin-top:10px;">Record</div>
#             <div style="font-size:32px; font-weight:700;">{record_value}</div>
#             <div style="font-size:14px; opacity:0.7; margin-top:10px;">Voiture</div>
#             <div style="font-size:25px; font-weight:700;">{car_value}</div>
#         </div>
#     """, unsafe_allow_html=True)

    # st.image("https://gpticketstore.vshcdn.net/uploads/images/15641/file.jpg", width=300)
    # st.metric("Record", record_value)

    

# with col2:
#     st.image("https://gpticketstore.vshcdn.net/uploads/images/15641/file.jpg", width=300)
#     st.metric("Voiture", car_value)







# st.header("Ici un header")
# st.subheader("subheader")


# st.markdown("---")

# st.text("Test d'un nouveau test ici en direct 2")
