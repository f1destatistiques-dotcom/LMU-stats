import streamlit as st

st.set_page_config(layout="wide") # Permet un affichage en plein écran

#Pour lancer l'environnement virtual
# cd virtenv
# streamlit run main.py

st.title("HOME - VROUUUM !")

# PERMET LA LECTURE DU FICHIER CSV STOCKÉ DANS LES DÉPÔTS DE GITHUB (MES PROPRES DÉPOTS)
import pandas as pd
url_general_data = "https://raw.githubusercontent.com/f1destatistiques-dotcom/LMU-stats/refs/heads/main/general_data.csv"
df_general_data = pd.read_csv(url_general_data)

# AFFICHER TOUT LE TABLEAU CSV
st.dataframe(df_general_data)

## AJUSTEMENT DU FORMAT DES CHIFFRES AFFICHÉS (évite les .0 pour chiffres entiers et limite à 2 décimales)
def format_value(v):
    try:
        v = float(v)
        if v.is_integer():
            return str(int(v))  # pas de .0
        else:
            return f"{v:.2f}"   # 2 décimales
    except:
        return str(v)

# CHOIX DES ICONES POUR LES TUILES
icons = {
    "Nombre de courses en multi": "🌐",
    "Nombre de tour": "🔁",
    "Nombre de victoires": "🏆",
    "Nombre de podiums": "🥉",
    "Nombre de TOP 5 / Ratio": "🏎️",
    "Nombre de de TOP 10 / Ratio": "🚥",

    "Nombre de poles": "🎯",
    "Ratio TOP 5": "📊",
    "Ratio TOP 10": "📈"
}

# Nombre de tuiles par ligne
tiles_per_row = 3

# TILES POPULATING
for i in range(0, len(df_general_data), tiles_per_row):
    cols = st.columns(tiles_per_row)

    for j in range(tiles_per_row):
        if i + j < len(df_general_data):
            row = df_general_data.iloc[i + j]
            label = row["Data"]
            value = row["Value"]
            icon = icons.get(label, "❓")

            with cols[j]:
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







st.header("Ici un header")
st.subheader("subheader")


st.markdown("---")

st.text("Test d'un nouveau test ici en direct 2")
