import streamlit as st

st.set_page_config(layout="wide")

# PERMET LA LECTURE DU FICHIER CSV STOCKÉ DANS LES DÉPÔTS DE GITHUB (MES PROPRES DÉPOTS)
import pandas as pd
url = "https://raw.githubusercontent.com/f1destatistiques-dotcom/LMU-stats/refs/heads/main/records.csv"
df = pd.read_csv(url)


# Choisir les colonnes du CSV à afficher
#colonnes = ["Circuit", "Voiture", "Record"]
#df_filtre = df[colonnes]
#st.dataframe(df_filtre)

# FILTRE SUR UNE VOITURE
# Voiture = st.selectbox("Choisir une voiture :", df["Voiture"].unique())
# df_filtre = df[df["Voiture"] == Voiture]
# st.dataframe(df_filtre)

# FILTRE SUR UNE VOITURE AVEC LA POSSIBILITÉ DE L'IGNORER
Voiture = st.selectbox("Voiture :", ["Toutes"] + list(df["Voiture"].unique()))
df_filtre = df[df["Voiture"] == Voiture]

if Voiture != "Toutes":
    df_filtre = df[df["Voiture"] == Voiture]
    st.dataframe(df_filtre)

# AFFICHER UNE VALEUR DANS UNE TUILE
record_value = df_filtre["Record"].iloc[0]
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

car_value = df_filtre["Voiture"].iloc[0]

with col1:
    st.markdown(f"""
        <div style="
            background-color:#D6D6D6;
            padding:15px;
            border-radius:12px;
            text-align:center;
            color:black ;">
            <img src="https://gpticketstore.vshcdn.net/uploads/images/15641/file.jpg" style="width:100%; border-radius:8px;">
            <div style="font-size:14px; opacity:0.7; margin-top:10px;">Record</div>
            <div style="font-size:32px; font-weight:700;">{record_value}</div>
            <div style="font-size:14px; opacity:0.7; margin-top:10px;">Voiture</div>
            <div style="font-size:25px; font-weight:700;">{car_value}</div>
        </div>
    """, unsafe_allow_html=True)

    # st.image("https://gpticketstore.vshcdn.net/uploads/images/15641/file.jpg", width=300)
    # st.metric("Record", record_value)

    

with col2:
    st.image("https://gpticketstore.vshcdn.net/uploads/images/15641/file.jpg", width=300)
    st.metric("Voiture", car_value)




# AFFICHER TOUT LE TABLEAU CSV
#st.dataframe(df)

st.title("Hi everyone, i'm one the place")
st.header("Ici un header")
st.subheader("subheader")


st.markdown("---")

st.text("Test d'un nouveau test ici en direct 2")
